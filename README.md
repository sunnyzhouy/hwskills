# hwskills

Huawei-style strategy, market, product, service, and transformation skill family for Codex.

[中文说明](README.zh-CN.md)

## Included skill families

This repo currently includes two parallel sets of Huawei-oriented skills under [skills](skills):

- English:
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

- Chinese:
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

## Project structure

- [skills](skills): skill folders ready to be installed or copied into a Codex skills directory
- [docs/audits](docs/audits): audit reports and comparative reviews

## Install

Copy the desired skill folders into your Codex skills directory:

```bash
cp -R skills/* "${CODEX_HOME:-$HOME/.codex}/skills/"
```

## Notes

- This repo only vendors the Huawei-oriented skill family.
- Comparative audit notes against gstack are preserved in [docs/audits/2026-03-27-skill-system-audit.md](docs/audits/2026-03-27-skill-system-audit.md).
- gstack skill code is not copied into this repository.
