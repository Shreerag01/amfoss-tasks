fn main() {
    let (mut name, mut price, mut tfh_change, mut tfh_volume, mut market_cap) 
                = (Vec::new(), Vec::new(), Vec::new(), Vec::new(), Vec::new());

    let url = "https://crypto.com/price";
    let response = reqwest::blocking::get(url).expect("Could not load url.");
    let body = response.text().unwrap();
    let document = scraper::Html::parse_document(&body);


    let name_selector = scraper::Selector::parse("div.css-ttxvk0>p").unwrap();
    let names = document.select(&name_selector).map(|x| x.inner_html());
    names
        .zip(0..50)
        .for_each(|(item, _number)| name.push(item) );

    
    let price_selector = scraper::Selector::parse("div.css-16q9pr7>div").unwrap();
    let prices= document.select(&price_selector).map(|x| x.inner_html());
    prices
        .zip(0..50)
        .for_each(|(item, _number)| price.push(item));


    let tfh_change_selector = scraper::Selector::parse("td.css-1b7j986>p").unwrap();
    let changes = document.select(&tfh_change_selector).map(|x| x.inner_html());
    changes
        .zip(0..50)
        .for_each(|(item, _number)| tfh_change.push(item));

        
    let market_cap_selector = scraper::Selector::parse("td.css-1nh9lk8").unwrap();
    let caps = document.select(&market_cap_selector).map(|x| x.inner_html());
    caps
        .zip(0..100)
        .for_each(|(item, _number)| 
        if _number%2 == 0 {
           market_cap.push(item)
         
        }
        else{
            tfh_volume.push(item)
        });

    let mut wtr = csv::Writer::from_path("crypto.csv").unwrap();
    wtr.write_record(&["No.","Name", "Price", "24H-Change","24H-Volume","Market-cap"]).expect("Could not write header.");
 
    for i in 0..50 {    
        let n: String = (i+1).to_string();
        wtr.write_record([&n, &name[i], &price[i], &tfh_change[i], &tfh_volume[i], &market_cap[i]]).expect("Could not create selector.");
    } 
    wtr.flush().expect("Could not close file");
}