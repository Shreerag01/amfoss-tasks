using System;
using System.Net;
using System.Net.Sockets;
using System.Text;

public class SynchronousSocketClient{

    public static void StartClient(){

        byte[] bytes = new byte[1024];

        try{

            IPHostEntry ipHostInfo = Dns.GetHostEntry(Dns.GetHostName());
            IPAddress ipAddress = ipHostInfo.AddressList[0];
            IPEndPoint remoteEP = new IPEndPoint(ipAddress, 11000);

            Socket sender = new Socket(ipAddress.AddressFamily, SocketType.Stream, ProtocolType.Tcp);

            try{
                sender.Connect(remoteEP);

                Console.WriteLine("Enter the Person Name: ");
                var name = Console.ReadLine();
                Console.WriteLine("Enter the Person Intrest: ");
                var intrests = Console.ReadLine();
                Console.WriteLine("Enter the Person Email: ");
                var mail = Console.ReadLine();

                byte[] msg = Encoding.ASCII.GetBytes(name + "," + intrests + "," + mail);

                int bytesSent = sender.Send(msg);

                sender.Shutdown(SocketShutdown.Both);
                sender.Close();

            }
            catch (ArgumentNullException ane){
                Console.WriteLine("ArgumentNullException : {0}", ane.ToString());
            }
            catch (SocketException se){
                Console.WriteLine("SocketException : {0}", se.ToString());
            }
            catch (Exception e){
                Console.WriteLine("Unexpected exception : {0}", e.ToString());
            }

        }
        catch (Exception e){
            Console.WriteLine(e.ToString());
        }
    }

    public static int Main(String[] args){
        StartClient();
        return 0;
    }
}
