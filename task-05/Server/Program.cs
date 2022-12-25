using System;
using System.Net;
using System.Net.Sockets;
using System.Text;

public class SynchronousSocketListener{

    public static string? data = null;

    public static void StartListening(){

        byte[] bytes = new Byte[1024];

        IPHostEntry ipHostInfo = Dns.GetHostEntry(Dns.GetHostName());
        IPAddress ipAddress = ipHostInfo.AddressList[0];
        IPEndPoint localEndPoint = new IPEndPoint(ipAddress, 11000);

        Socket listener = new Socket(ipAddress.AddressFamily, SocketType.Stream, ProtocolType.Tcp);

        string fileName = "file.json";
        try{
            listener.Bind(localEndPoint);
            listener.Listen(10);

            while (true){
                Console.WriteLine("Waiting for a connection...");

                Socket handler = listener.Accept();
                string? data = null;
                int bytesRec = handler.Receive(bytes);
                data = Encoding.ASCII.GetString(bytes,0,bytesRec);

                Console.WriteLine("Text received : {0}", data);

                byte[] msg = Encoding.ASCII.GetBytes(data);

                string[] dataArr = data.Split(',');
                string name = dataArr[0];
                string intrests = dataArr[1];
                string mail = dataArr[2];
                string jsonData = "{ \"name\": \"" + name + "\", \"intrests\": \"" + intrests + "\", \"mail\": \"" + mail + "\" }";
                Console.WriteLine("Name: {0}", name);
                Console.WriteLine("Intrests: {0}", intrests);
                Console.WriteLine("Email: {0}", mail);
                if (File.Exists(fileName)){
                    using (StreamWriter sw = File.AppendText(fileName)){
                        sw.WriteLine(jsonData);
                    }
                }
                else{
                    using (StreamWriter sw = File.CreateText(fileName)){
                        sw.WriteLine(jsonData);
                    }
                }
                handler.Shutdown(SocketShutdown.Both);
                handler.Close();
            }

        }
        catch (Exception e){
            Console.WriteLine(e.ToString());
        }

        Console.WriteLine("\nPress ENTER to continue...");
        Console.Read();

    }

    public static int Main(String[] args){
        StartListening();
        return 0;
    }
}