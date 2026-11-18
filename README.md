# pairwise-subsurface-scattering

角色耳朵和鼻尖在逆光下像塑料、蜡像透光过强、阴影里发红：扩散用单指数；厚度图按顶点法线；次表面颜色和反照率混用；透光只算主光；曲率没参与；皮肤遮蔽和 SSS 重复；半透明物体排序后仍写深度；预积分 LUT 按错参数；散射半径随分辨率变；多光源能量不归一。render/subsurface_scattering.py 是核心，tests/test_subsurface_scattering.py 15个红。要修的是：多指数扩散；厚度按光线方向；分离散射色；全部光源透光；曲率加权；遮蔽去重；透明深度写；LUT 参数校准；世界单位半径；多光归一。

## 运行

```bash
python -m pytest tests -q
```

初始状态：15 个用例失败。修复实现使全部用例通过，不要修改 `tests/` 下的测试。

子方向：图形渲染；任务类型：Bugfix；语言/框架：Python 3, pytest；环境可复现等级：无外部依赖。
