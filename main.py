import RT_utility as rtu
import RT_camera as rtc
import RT_renderer as rtren
import RT_material as rtm
import RT_scene as rts
import RT_object as rto
import RT_integrator as rti
import RT_light as rtl
import RT_texture as rtt

def renderProceduralTexture():
    main_camera = rtc.Camera()
    main_camera.aspect_ratio = 16.0/9.0
    main_camera.img_width = 400
    main_camera.center = rtu.Vec3(0,0,0)
    main_camera.samples_per_pixel = 20
    main_camera.max_depth = 5
    main_camera.vertical_fov = 60
    main_camera.look_from = rtu.Vec3(-2, 2, 1)
    main_camera.look_at = rtu.Vec3(0, 0, -1)
    main_camera.vec_up = rtu.Vec3(0, 1, 0)

    defocus_angle =0.0
    focus_distance = 10.0
    main_camera.init_camera(defocus_angle, focus_distance)
    # add objects to the scene

    mat_center = rtm.Lambertian(rtu.Color(0.7, 0.3, 0.3))

    # create textures
    mat_tex_checker_bw = None   # black and white checker board
    mat_tex_checker = None      # colorful checker board
    mat_tex_solid = None        # solid color

    world = rts.Scene()
    world.add_object(rto.Sphere(rtu.Vec3(   0,-100.5,-1),  100, mat_tex_checker_bw))
    world.add_object(rto.Sphere(rtu.Vec3(   0,   0.0,-1),  0.5, mat_center))
    world.add_object(rto.Sphere(rtu.Vec3(-1.0,   0.0,-1),  0.5, mat_tex_checker))
    world.add_object(rto.Sphere(rtu.Vec3( 1.0,   0.0,-1),  0.5, mat_tex_solid))

    intg = rti.Integrator()

    renderer = rtren.Renderer(main_camera, intg, world)
    renderer.render()
    renderer.write_img2png('week07_texture_sky.png')    

def renderEarth():
    main_camera = rtc.Camera()
    main_camera.aspect_ratio = 16.0/9.0
    main_camera.img_width = 400
    main_camera.center = rtu.Vec3(0,0,0)
    main_camera.samples_per_pixel = 20
    main_camera.max_depth = 5
    main_camera.vertical_fov = 60
    main_camera.look_from = rtu.Vec3(-2, 2, 1)
    main_camera.look_at = rtu.Vec3(0, 0, -1)
    main_camera.vec_up = rtu.Vec3(0, 1, 0)

    defocus_angle =0.0
    focus_distance = 10.0
    main_camera.init_camera(defocus_angle, focus_distance)
    # add objects to the scene

    mat_tex_checker_bw = None   # black and white checker board
    mat_tex_earth = None        # earth texture
    mat_tex_basketball = None   # basketball
    mat_tex_soccer = None       # soccer
    mat_tex_pepsi = None        # pepsi logo

    world = rts.Scene()
    world.add_object(rto.Sphere(rtu.Vec3(   0,-100.5,-1),  100, mat_tex_earth))
    world.add_object(rto.Sphere(rtu.Vec3(   0,   0.0,-1),  0.5, mat_tex_checker_bw))
    world.add_object(rto.Sphere(rtu.Vec3(-1.0,   0.0,-1),  0.5, mat_tex_basketball))
    world.add_object(rto.Sphere(rtu.Vec3( 1.0,   0.0,-1),  0.5, mat_tex_soccer))

    world.add_object(rto.Quad(rtu.Vec3(1.0, 0.0, -1), rtu.Vec3(1.0, 2.0, -1), rtu.Vec3(1.0, 0.0, 1), mat_tex_pepsi))

    intg = rti.Integrator()

    renderer = rtren.Renderer(main_camera, intg, world)
    renderer.render()
    renderer.write_img2png('week07_texture_earth_sky.png')    

def renderMetals():
    main_camera = rtc.Camera()
    main_camera.aspect_ratio = 16.0/9.0
    main_camera.img_width = 400
    main_camera.center = rtu.Vec3(0,0,0)
    main_camera.samples_per_pixel = 30
    main_camera.max_depth = 5
    main_camera.vertical_fov = 60
    main_camera.look_from = rtu.Vec3(-2, 2, 1)
    main_camera.look_at = rtu.Vec3(0, 0, -1)
    main_camera.vec_up = rtu.Vec3(0, 1, 0)

    defocus_angle =0.0
    focus_distance = 10.0
    main_camera.init_camera(defocus_angle, focus_distance)
    # add objects to the scene

    tex_checker_bw = rtt.CheckerTexture(0.32, rtu.Color(.2, .2, .2), rtu.Color(.9, .9, .9))
    mat_tex_checker_bw = rtm.TextureColor(tex_checker_bw)

    mat_metal1 = rtm.Metal(rtu.Color(0.7, 0.2, 0.4), 1)
    mat_metal2 = rtm.Metal(rtu.Color(0.7, 0.2, 0.4), 0.3)
    mat_metal3 = rtm.Metal(rtu.Color(0.7, 0.2, 0.4), 0.05)

    world = rts.Scene()
    world.add_object(rto.Sphere(rtu.Vec3(   0,-100.5,-1),  100, mat_tex_checker_bw))
    world.add_object(rto.Sphere(rtu.Vec3(-1.0,   0.0,-1),  0.5, mat_metal2))    # left
    world.add_object(rto.Sphere(rtu.Vec3(   0,   0.0,-1),  0.5, mat_metal1))    # center
    world.add_object(rto.Sphere(rtu.Vec3( 1.0,   0.0,-1),  0.5, mat_metal3))    # right

    dlight = rtl.Diffuse_light(rtu.Color(0.8, 0.8, 0.8))
    world.add_object(rto.Quad(rtu.Vec3(-0.5,1.5,-0.5), rtu.Vec3(0,0,-7.5), rtu.Vec3(1,0,-0.5), dlight))

    intg = rti.Integrator()

    renderer = rtren.Renderer(main_camera, intg, world)
    renderer.render()
    renderer.write_img2png('week07_metals.png')    

def renderBRDFs():
    main_camera = rtc.Camera()
    main_camera.aspect_ratio = 16.0/9.0
    main_camera.img_width = 400
    main_camera.center = rtu.Vec3(0,0,0)
    main_camera.samples_per_pixel = 512
    main_camera.max_depth = 5
    main_camera.vertical_fov = 60
    main_camera.look_from = rtu.Vec3(-2, 2, 1)
    main_camera.look_at = rtu.Vec3(0, 0, -1)
    main_camera.vec_up = rtu.Vec3(0, 1, 0)

    defocus_angle =0.0
    focus_distance = 10.0
    main_camera.init_camera(defocus_angle, focus_distance)
    # add objects to the scene

    tex_checker_bw = rtt.CheckerTexture(0.32, rtu.Color(.2, .2, .2), rtu.Color(.9, .9, .9))
    tex_checker = rtt.CheckerTexture(0.12, rtu.Color(.2, .3, .1), rtu.Color(.9, .9, .9))
    tex_solid = rtt.SolidColor(rtu.Color(0.2, 0.2, 0.5))

    mat_tex_checker_bw = rtm.TextureColor(tex_checker_bw)

    mat_phong1 = rtm.Phong(rtu.Color(0.7, 0.2, 0.4), 0.3, 0.6, 0.008)
    mat_phong2 = rtm.Phong(rtu.Color(0.7, 0.2, 0.4), 0.3, 0.6, 0.08)
    mat_phong3 = rtm.Phong(rtu.Color(0.7, 0.2, 0.4), 0.3, 0.6, 0.8)

    world = rts.Scene()
    world.add_object(rto.Sphere(rtu.Vec3(   0,-100.5,-1),  100, mat_tex_checker_bw))
    world.add_object(rto.Sphere(rtu.Vec3(-1.0,   0.0,-1),  0.5, mat_phong1))    # left
    world.add_object(rto.Sphere(rtu.Vec3(   0,   0.0,-1),  0.5, mat_phong2))    # center
    world.add_object(rto.Sphere(rtu.Vec3( 1.0,   0.0,-1),  0.5, mat_phong3))    # right

    dlight = rtl.Diffuse_light(rtu.Color(0.8, 0.8, 0.8))
    world.add_object(rto.Quad(rtu.Vec3(-0.5,1.5,-0.5), rtu.Vec3(0,0,-7.5), rtu.Vec3(1,0,-0.5), dlight))

    intg = rti.Integrator()

    renderer = rtren.Renderer(main_camera, intg, world)
    renderer.render()
    renderer.write_img2png('week07_brdf_Phong.png')    

if __name__ == "__main__":
    # renderProceduralTexture()
    # renderEarth()
    renderMetals()
    # renderBRDFs()


