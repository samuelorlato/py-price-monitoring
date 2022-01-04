# A Python price monitor 

> This project was focused on Brazil, so the monitoring is of "Mercado Livre" product prices

### How to use?
1. Follow this "template":
 `python main.py --to-email emailtoreceive@email.com --product-url https://mercadolivreurl.com --target-price 2000 --from-email fromemail@email.com --from-email-password password`
      
2. Some explanations:
     - **--to-email**: Email that you will receive the notifications
     - **--product-url**: The Mercado Livre product URL, like: https://www.mercadolivre.com.br/samsung-galaxy-a32-dual-sim-128-gb-azul-4-gb-ram/p/MLB17465173?pdp_filters=category:MLB1055#searchVariation=MLB17465173&position=1&search_layout=stack&type=product&tracking_id=0acc80d9-4ebd-4304-9fce-ba94cd1f06ad
     - **--target-price**: From the price you want be notified
     - **--from-email**: Email that will send you the notifications
     - **--from-email-password**: Password for the email that will send the notifications (**Important**: In gmail you need to activate the access to less secure apps)

3. Constant monitoring:
     - Use something like [crontab](https://www.tutorialspoint.com/unix_commands/crontab.htm) or a 24/7 server

4. Installation:
     - Dependecies:
          - Beautiful Soup: `pip install bs4`
          - Requests: `pip install requests`
          - Typer: `pip install typer` 
         
     - `git clone https://github.com/OrlatoDev/py-price-monitoring.git`
     - `cd py-price-monitoring`
     - `python ./main.py` and follow the "template"
