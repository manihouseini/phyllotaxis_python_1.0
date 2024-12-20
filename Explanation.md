# Spiral Phyllotaxis

In spiral phyllotaxy, the individual floral organs are created in a regular time interval with the same divergent angle. The divergent angle in a flower with spiral phyllotaxy approximates 137.5 degrees, which is indicative of a pattern that follows a Fibonacci series.
Other types of floral phyllotaxic arrangements are:

Whorled Phyllotaxis,<br>
Simple-whorled Phyllotaxis,<br>
Complex-whorled Phyllotaxis &<br>
Irregular Phyllotaxis

- for num in (number of points):
  - distFromCenter = spread \* sqrt(num)
  - θ = num \* angleRad(137.508°)
  - x = distFromCenter \* cos(θ)
  - y = distFromCenter \* sin(θ)

other known angles that make interesting patterns other than 137.508° include:

- normal spiral phyllotaxis: 137.508°
- distichy: 180°
- anomalous phyllotaxis: 99.5°
- tristichy: 120°
