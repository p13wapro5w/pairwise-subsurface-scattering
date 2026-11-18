"""第 53 批：角色耳朵和鼻尖在逆光下像塑料、蜡像透光过强、阴影..."""

def diffusion(distance, radius):
    """返回多指数扩散衰减。"""
    raise NotImplementedError("TODO: diffusion")

def thickness_along(normal, light):
    """返回沿光线方向的介质厚度。"""
    raise NotImplementedError("TODO: thickness_along")

def scatter_color(albedo, sss):
    """分离反照率与次表面散射色。"""
    raise NotImplementedError("TODO: scatter_color")

def transmittance(light, thickness):
    """返回透射光强。"""
    raise NotImplementedError("TODO: transmittance")

def curvature_weight(curvature):
    """按曲率返回散射权重。"""
    raise NotImplementedError("TODO: curvature_weight")

def shadow_dedupe(shadow, sss):
    """合并皮肤遮蔽与次表面贡献。"""
    raise NotImplementedError("TODO: shadow_dedupe")

def write_depth(transparent, depth_write):
    """判断透明物体是否写深度。"""
    raise NotImplementedError("TODO: write_depth")

def lut_param(curvature, radius):
    """返回预积分 LUT 参数。"""
    raise NotImplementedError("TODO: lut_param")

def world_radius(pixels, pixels_per_unit):
    """把像素半径换算成世界单位。"""
    raise NotImplementedError("TODO: world_radius")
