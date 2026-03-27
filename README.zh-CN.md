# hwskills

面向 Codex 的华为式战略、市场、产品、服务与变革方法 skill 集合。

[English](README.md)

## 包含的 skill 家族

当前仓库在 [skills](skills) 目录下包含两套并行的华为方法 skill：

- 英文版：
  - `leadership-intent-decoder`
  - `huawei-methods`
  - `huawei-strategy-principles`
  - `huawei-market-principles`
  - `huawei-product-principles`
  - `huawei-service-principles`
  - `strategy-blm-dste-execution`
  - `market-management-execution`
  - `product-planning-execution`
  - `product-development-ipd-execution`
  - `sales-ltc-execution`
  - `service-itr-execution`
  - `transformation-pmo-execution`

- 中文版：
  - `zh-leadership-intent-decoder`
  - `zh-huawei-methods`
  - `zh-huawei-strategy-principles`
  - `zh-huawei-market-principles`
  - `zh-huawei-product-principles`
  - `zh-huawei-service-principles`
  - `zh-strategy-blm-dste-execution`
  - `zh-market-management-execution`
  - `zh-product-planning-execution`
  - `zh-product-development-ipd-execution`
  - `zh-sales-ltc-execution`
  - `zh-service-itr-execution`
  - `zh-transformation-pmo-execution`

## 项目结构

- [skills](skills)：可直接安装或复制到 Codex skills 目录的 skill 文件夹
- [docs/audits](docs/audits)：审计报告和对比评审材料

## 安装

把所需的 skill 目录复制到你的 Codex skills 目录：

```bash
cp -R skills/* "${CODEX_HOME:-$HOME/.codex}/skills/"
```

## 说明

- 本仓库只收录华为方法论 skill 家族。
- 与 gstack 的对比审计报告保存在 [docs/audits/2026-03-27-skill-system-audit.md](docs/audits/2026-03-27-skill-system-audit.md)。
- 本仓库未拷贝 gstack 的 skill 源码。
