# MOSFET Current Source

Made a current source using a [IRLD024 Power MOSFET](https://www.vishay.com/docs/91308/sihld24.pdf).
Checking the [datasheet for the LED](https://www.ttelectronics.com/TTElectronics/media/ProductFiles/Optoelectronics/Datasheets/OVLL.pdf) now I see the maximum continuous current is 50mA. I thought it was 70 mA.

![](currentSource.png)

## Data File

Data was taken with a DMM. 

* Vin was measured between the gate and ground.
* Vres was measured across the resistor.
* I<sub>LED</sub> was calculated by dividing Vres by 10.

## Plot Current vs Vin

There appear to be a couple errant points.

![](vinPlot.png)

The plot was created using the python script [plot-LED-current.py](plot-LED-current.py).

## Plot Current vs Vgs

There appear to be a couple errant points.

![](vgsPlot.png)

The plot was created using the python script [plot-LED-current-vgs.py](plot-LED-current-vgs.py)
