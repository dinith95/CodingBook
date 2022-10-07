## sample format 

![Cron Expression ](../images/cron.png?raw=true "Cron Expression format")


## symbol definition 

### * - any value 

### , - values seperator 

    eg : * 2,4 * * * - Every miniute in hour 2 and 4 

### - range 

    eg : * 2-4 * * * - every minute passes from hour 2 to 4 

### - create a step for each values 

    eg : 1/10 * * * * - every 10th miniute in all hours \
         30\10 * * * * -   every 10th minute starting from 30 miniutes omward
        * 12/6 * * *  -  minute passed every hour from 12 noon to 12 mdnight any date 