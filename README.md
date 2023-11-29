# RT-python-week08
Ray tracing course week 08

This repository is for 'Raytracing in Entertainment Industry' (01418283).
This course is set to be taught for undergrad students at Dept of Computer Science, Faculty of Science, Kasetsart University.
The codes were rewritten and modified from https://raytracing.github.io/books/RayTracingInOneWeekend.html.

**Prerequisites :**
1. C/C++ or python.
2. Object-Oriented Programming (OOP).
3. Linear algebra for undergrad students.


**Class assignment**

Note that to submit the rendered results, please use the following parameters.
- at least 100 samples per pixel.
- at least 5 max depth.
- resolution width = 480p.
- aspect ratio = 16:9.
- sky as the background.
- No light is needed. 

1. Complete 'scattering()' method in the 'class Phong(Material)' to represent the Phong BRDF.
    - render a scene with 3 balls in the scene. Each ball exhibits a Phong material with roughness parameters = 0.8, 0.08 and 0.008.
    - save the rendered image to 'week08_Phong.png' and submit the rendered file. 
2. Implement 'class Blinn(Material)'.
    - render a scene with 3 balls in the scene. Each ball exhibits a Blinn material with roughness parameters = 0.8, 0.08 and 0.008.
    - save the rendered image to 'week08_Blinn.png' and submit the rendered file. 
3. Implement 'class CookTorrance(Material)'.
    - render a scene with 3 balls in the scene. Each ball exhibits a Cook-Torrance material with .
    - save the rendered image to 'week08_CookTorance.png' and submit the rendered file. 

