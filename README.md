#TwistedBrew

Twisted Brew - Distributed brewing Software

This project is still in early design stages. 
More info will be added when it starts to take shape.

Design goals:

* Scalable brewing solution that can run on one or more devices
* The ability to read and use recipe info from [Beersmith](http://beersmith.com/)
* Server/Client design, one BrewMaster to rule them all (his workers) 

Master:

*   Parses recipe.bsmx from Beersmith and collects marsh schedule, hop schedule and fermentation schedule
*   Can be monitored and controlled from a web GUI
*   Collects info from all BrewWorkers on the network for the user to control
*   Can assign brewing schedule(s) to available brewWorkers

Worker:

* Can manipulate various devices (Initially: SSR (Heating/Cooling element, pump), TempProb. Future: Electronic valve, FlowMeter, Servo)
* Can follow brewing schedule(s) which are assigned by a Master

The Twisted Pair (hif & hJod)  

---

##Usefull information

To start the Twisted Brew master and worker modules from config file (default is config/twisted_brew.yml), run:

    python manage.py twisted_brew

To use a specific config file add it's path as an optional parameter to the above command, example:

    python manage.py twisted_brew config/my_config_file.yml

###The DS18B20 temperature probe

To be able to use the probe you have to enabling the 1-wire communication device kernel modules in linux. Here is how it is done in Debian (also Rasbian).

Run these commands: `sudo modprobe w1-gpio && sudo modprobe w1_therm`

and then add **w1-gpio** and **w1_therm** in **/etc/modules** so that the mod survives reboot.

Excellent information on how to connect and work with the DS18B20 on Rasberry Pi can be found on this [website](http://www.reuk.co.uk/DS18B20-Temperature-Sensor-with-Raspberry-Pi.htm).

###Browser requirements

As our gui uses .bind() method in Javascript you have to use the following browsers:

*   Chrome 7 or higher
*   Firefox 4.0(2) or higher
*   IE 9 or higher
*   Opera 11.60 or higher
*   Safari 5.1.4 or higher

Required packages
* Django
* pyYAML
* suit
* pytz
* pyzmq
* HTMLParser
