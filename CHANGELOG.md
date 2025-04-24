# Changelog

## 0.5.1 (2025-04-24)

Full Changelog: [v0.5.0...v0.5.1](https://github.com/aigc-libs/pyopenwebui-python/compare/v0.5.0...v0.5.1)

### Bug Fixes

* **ci:** ensure pip is always available ([#59](https://github.com/aigc-libs/pyopenwebui-python/issues/59)) ([9bcb1ad](https://github.com/aigc-libs/pyopenwebui-python/commit/9bcb1ad0a0c567c057aa12b4460b22f9fee66b05))
* **ci:** remove publishing patch ([#60](https://github.com/aigc-libs/pyopenwebui-python/issues/60)) ([97291e0](https://github.com/aigc-libs/pyopenwebui-python/commit/97291e0ccd55792429efa7c96c2705d4108371c6))
* **perf:** optimize some hot paths ([c83bce5](https://github.com/aigc-libs/pyopenwebui-python/commit/c83bce5c45b9ffcb1dfd07f27ed39129d7d2cf0b))
* **perf:** skip traversing types for NotGiven values ([3a54ba6](https://github.com/aigc-libs/pyopenwebui-python/commit/3a54ba62acb6214c59e2ebae54b8b0209a423059))
* **pydantic v1:** more robust ModelField.annotation check ([3af7dd3](https://github.com/aigc-libs/pyopenwebui-python/commit/3af7dd375f2ef25cd0e0cc217cd7be4ef3cd4ccc))
* **types:** handle more discriminated union shapes ([#58](https://github.com/aigc-libs/pyopenwebui-python/issues/58)) ([7d7ae2c](https://github.com/aigc-libs/pyopenwebui-python/commit/7d7ae2c55bba4d04f6e1fc6857ea4c3060e8c824))


### Chores

* broadly detect json family of content-type headers ([8006737](https://github.com/aigc-libs/pyopenwebui-python/commit/800673733f13c68b88cc48b0c74ad76fa2149cc8))
* **ci:** add timeout thresholds for CI jobs ([cb9760c](https://github.com/aigc-libs/pyopenwebui-python/commit/cb9760cac334d31c1c3cac67b4c1da446d35c991))
* **ci:** only use depot for staging repos ([b9e1d07](https://github.com/aigc-libs/pyopenwebui-python/commit/b9e1d072e068a12dd21aafeae686547427517e06))
* **client:** minor internal fixes ([c0ee9f8](https://github.com/aigc-libs/pyopenwebui-python/commit/c0ee9f890da000df20934096b445251250cc3790))
* fix typos ([#61](https://github.com/aigc-libs/pyopenwebui-python/issues/61)) ([351b5a2](https://github.com/aigc-libs/pyopenwebui-python/commit/351b5a2a2da8772b728317a4559429a6d497d1dc))
* **internal:** base client updates ([d63299f](https://github.com/aigc-libs/pyopenwebui-python/commit/d63299f41a37cf5e5d75a288b016967de4d256d8))
* **internal:** bump pyright version ([0db1edb](https://github.com/aigc-libs/pyopenwebui-python/commit/0db1edb0ae712fae3bdf558df35ef3e8c57413e9))
* **internal:** bump rye to 0.44.0 ([#57](https://github.com/aigc-libs/pyopenwebui-python/issues/57)) ([380c7e7](https://github.com/aigc-libs/pyopenwebui-python/commit/380c7e78e3de2c29b0995b3a27b98441f3411e6c))
* **internal:** codegen related update ([1fac880](https://github.com/aigc-libs/pyopenwebui-python/commit/1fac8802f622d32c8a69c470e126e70c0d14b559))
* **internal:** codegen related update ([#53](https://github.com/aigc-libs/pyopenwebui-python/issues/53)) ([d8d7279](https://github.com/aigc-libs/pyopenwebui-python/commit/d8d7279c8c59f94b2346cc4e514ea7061d0d9d80))
* **internal:** codegen related update ([#56](https://github.com/aigc-libs/pyopenwebui-python/issues/56)) ([f7f887c](https://github.com/aigc-libs/pyopenwebui-python/commit/f7f887cd3385016388105e08c9f2d100f8750070))
* **internal:** expand CI branch coverage ([c0b031e](https://github.com/aigc-libs/pyopenwebui-python/commit/c0b031e884e0108c7e8e40958afb5a30fca406cf))
* **internal:** fix list file params ([14895e8](https://github.com/aigc-libs/pyopenwebui-python/commit/14895e890ddd161b259be489300c768e28fe75d6))
* **internal:** import reformatting ([a26fe4f](https://github.com/aigc-libs/pyopenwebui-python/commit/a26fe4f75545b612b1cb774ef3fda5ec22deb699))
* **internal:** minor formatting changes ([8129a0c](https://github.com/aigc-libs/pyopenwebui-python/commit/8129a0c494c94012895bf59a31cbc992d3e2b77e))
* **internal:** minor test fixes ([#62](https://github.com/aigc-libs/pyopenwebui-python/issues/62)) ([7410e5d](https://github.com/aigc-libs/pyopenwebui-python/commit/7410e5da577b1cd69c5945112aac591b8d4f8c73))
* **internal:** reduce CI branch coverage ([3a419c5](https://github.com/aigc-libs/pyopenwebui-python/commit/3a419c561b14d9111662388b348e286daf6eab53))
* **internal:** refactor retries to not use recursion ([25358f7](https://github.com/aigc-libs/pyopenwebui-python/commit/25358f78d5b1550668ff58a0ea2e0086c75e4b0e))
* **internal:** remove extra empty newlines ([#55](https://github.com/aigc-libs/pyopenwebui-python/issues/55)) ([667f89a](https://github.com/aigc-libs/pyopenwebui-python/commit/667f89a7d783dd71c8bcc82dee2526e8002a94e9))
* **internal:** remove trailing character ([#63](https://github.com/aigc-libs/pyopenwebui-python/issues/63)) ([8d44fd8](https://github.com/aigc-libs/pyopenwebui-python/commit/8d44fd8ab529168ca1c7e87a2d2a3d82d7aeae5a))
* **internal:** slight transform perf improvement ([#64](https://github.com/aigc-libs/pyopenwebui-python/issues/64)) ([3e590b3](https://github.com/aigc-libs/pyopenwebui-python/commit/3e590b3a0b21fa86166146a005e37545cf4c97aa))
* **internal:** update models test ([b04f9dc](https://github.com/aigc-libs/pyopenwebui-python/commit/b04f9dc2187ec189e85e6bf8c3808d366a141f86))
* **internal:** update pyright settings ([0978550](https://github.com/aigc-libs/pyopenwebui-python/commit/0978550626d35b9fd236033ab83ac0471fd9a37c))
* slight wording improvement in README ([#65](https://github.com/aigc-libs/pyopenwebui-python/issues/65)) ([632ebcb](https://github.com/aigc-libs/pyopenwebui-python/commit/632ebcbf28ec93a10134a6d0d7930b143a77dff8))

## 0.5.0 (2025-03-08)

Full Changelog: [v0.4.0...v0.5.0](https://github.com/aigc-libs/pyopenwebui-python/compare/v0.4.0...v0.5.0)

### Features

* **api:** update via SDK Studio ([58760a2](https://github.com/aigc-libs/pyopenwebui-python/commit/58760a2500244b8c5624f7eb86794f693615f2b2))
* **api:** update via SDK Studio ([cb90dff](https://github.com/aigc-libs/pyopenwebui-python/commit/cb90dff53133f9c8ddbf25e57be7186d8f750286))
* **api:** update via SDK Studio ([0ea42bf](https://github.com/aigc-libs/pyopenwebui-python/commit/0ea42bfbb01913663e50d9e5f965a3d8e3d1f801))
* **api:** update via SDK Studio ([12d3f3f](https://github.com/aigc-libs/pyopenwebui-python/commit/12d3f3f1ce6f508e9725656f632f29287a806d0b))
* **api:** update via SDK Studio ([#50](https://github.com/aigc-libs/pyopenwebui-python/issues/50)) ([a20862b](https://github.com/aigc-libs/pyopenwebui-python/commit/a20862b2fd41587723b15acb2e7a1510edfbac04))

## 0.4.0 (2025-03-08)

Full Changelog: [v0.3.22...v0.4.0](https://github.com/aigc-libs/pyopenwebui-python/compare/v0.3.22...v0.4.0)

### Features

* **api:** update via SDK Studio ([#46](https://github.com/aigc-libs/pyopenwebui-python/issues/46)) ([b3a6c2e](https://github.com/aigc-libs/pyopenwebui-python/commit/b3a6c2e23c79114420a268a05470ef12e416830e))
* **api:** update via SDK Studio ([#48](https://github.com/aigc-libs/pyopenwebui-python/issues/48)) ([efb974b](https://github.com/aigc-libs/pyopenwebui-python/commit/efb974b1599eb4bb707086024a36b95d07dadeee))

## 0.3.22 (2025-01-25)

Full Changelog: [v0.3.21...v0.3.22](https://github.com/aigc-libs/pyopenwebui-python/compare/v0.3.21...v0.3.22)

### Bug Fixes

* **client:** compat with new httpx 0.28.0 release ([#18](https://github.com/aigc-libs/pyopenwebui-python/issues/18)) ([049072f](https://github.com/aigc-libs/pyopenwebui-python/commit/049072f0ff756f9ea31d7e1a2a4c99b250ef709c))
* **client:** only call .close() when needed ([#34](https://github.com/aigc-libs/pyopenwebui-python/issues/34)) ([36403bb](https://github.com/aigc-libs/pyopenwebui-python/commit/36403bbf0f35f45084cd54cbaa3a046dbce2d0bc))
* correctly handle deserialising `cls` fields ([#36](https://github.com/aigc-libs/pyopenwebui-python/issues/36)) ([db9fac4](https://github.com/aigc-libs/pyopenwebui-python/commit/db9fac4d450d3a6d14aa11cafe91d0000f6e63c6))
* **tests:** make test_get_platform less flaky ([#40](https://github.com/aigc-libs/pyopenwebui-python/issues/40)) ([4d76b93](https://github.com/aigc-libs/pyopenwebui-python/commit/4d76b9310ad0743a0d320d7bfc9e18610061a6ce))


### Chores

* **internal:** add support for TypeAliasType ([#24](https://github.com/aigc-libs/pyopenwebui-python/issues/24)) ([dd417b3](https://github.com/aigc-libs/pyopenwebui-python/commit/dd417b38a27a56cf42960e0eae4a9352d837401b))
* **internal:** avoid pytest-asyncio deprecation warning ([#41](https://github.com/aigc-libs/pyopenwebui-python/issues/41)) ([68e90fa](https://github.com/aigc-libs/pyopenwebui-python/commit/68e90faa5333a06200e7d896c58e52cda59eb8e2))
* **internal:** bump httpx dependency ([#33](https://github.com/aigc-libs/pyopenwebui-python/issues/33)) ([ed64e14](https://github.com/aigc-libs/pyopenwebui-python/commit/ed64e14274fd26c1485b89993f35b3d04f4041e7))
* **internal:** bump pydantic dependency ([#21](https://github.com/aigc-libs/pyopenwebui-python/issues/21)) ([626883a](https://github.com/aigc-libs/pyopenwebui-python/commit/626883ab49a2b396a7e22492d4b45d34dd10edda))
* **internal:** bump pyright ([#23](https://github.com/aigc-libs/pyopenwebui-python/issues/23)) ([1f4e567](https://github.com/aigc-libs/pyopenwebui-python/commit/1f4e5671b846ab127ed688da50597bc4a109a5dd))
* **internal:** codegen related update ([#19](https://github.com/aigc-libs/pyopenwebui-python/issues/19)) ([2072439](https://github.com/aigc-libs/pyopenwebui-python/commit/20724395c7dd2aa1f8f717504177da606e709717))
* **internal:** codegen related update ([#25](https://github.com/aigc-libs/pyopenwebui-python/issues/25)) ([f9aca77](https://github.com/aigc-libs/pyopenwebui-python/commit/f9aca77705f5443b7375a63682d8457eab9470e7))
* **internal:** codegen related update ([#26](https://github.com/aigc-libs/pyopenwebui-python/issues/26)) ([f46b1f0](https://github.com/aigc-libs/pyopenwebui-python/commit/f46b1f0c84f32777472f9649c2639a785a246820))
* **internal:** codegen related update ([#31](https://github.com/aigc-libs/pyopenwebui-python/issues/31)) ([fce3014](https://github.com/aigc-libs/pyopenwebui-python/commit/fce30141e81edc964eec32142407eddd16bb5889))
* **internal:** codegen related update ([#32](https://github.com/aigc-libs/pyopenwebui-python/issues/32)) ([47cd339](https://github.com/aigc-libs/pyopenwebui-python/commit/47cd3392e58d5d0d34eab781a0af558e9a0ed897))
* **internal:** codegen related update ([#35](https://github.com/aigc-libs/pyopenwebui-python/issues/35)) ([b3eee85](https://github.com/aigc-libs/pyopenwebui-python/commit/b3eee854a71566bb6ae8f690023a50386f69eae1))
* **internal:** codegen related update ([#37](https://github.com/aigc-libs/pyopenwebui-python/issues/37)) ([8c77819](https://github.com/aigc-libs/pyopenwebui-python/commit/8c778197cfacd70391b778652b03109da2388cc5))
* **internal:** codegen related update ([#38](https://github.com/aigc-libs/pyopenwebui-python/issues/38)) ([8ce52a1](https://github.com/aigc-libs/pyopenwebui-python/commit/8ce52a1d756fced14ae17a46c1b2369bd8d37f0c))
* **internal:** codegen related update ([#42](https://github.com/aigc-libs/pyopenwebui-python/issues/42)) ([8cbaa73](https://github.com/aigc-libs/pyopenwebui-python/commit/8cbaa7397935b98eeedf41c0784be5bb44ded55f))
* **internal:** codegen related update ([#43](https://github.com/aigc-libs/pyopenwebui-python/issues/43)) ([986e14e](https://github.com/aigc-libs/pyopenwebui-python/commit/986e14ef258f43757b589168c784498d59888f37))
* **internal:** exclude mypy from running on tests ([#17](https://github.com/aigc-libs/pyopenwebui-python/issues/17)) ([2609c58](https://github.com/aigc-libs/pyopenwebui-python/commit/2609c582be9c465b12397fd383ad95ff5f3daefb))
* **internal:** fix compat model_dump method when warnings are passed ([#13](https://github.com/aigc-libs/pyopenwebui-python/issues/13)) ([3f58707](https://github.com/aigc-libs/pyopenwebui-python/commit/3f5870789a7e966e0ea1d183ff1b2c2743fa7c05))
* **internal:** fix some typos ([#30](https://github.com/aigc-libs/pyopenwebui-python/issues/30)) ([a4a7087](https://github.com/aigc-libs/pyopenwebui-python/commit/a4a70879341f0fcd53db39e03a42e98cee7143d3))
* **internal:** remove some duplicated imports ([#27](https://github.com/aigc-libs/pyopenwebui-python/issues/27)) ([2b9d923](https://github.com/aigc-libs/pyopenwebui-python/commit/2b9d923ec0db4d3e262289a9160ca527547d8594))
* **internal:** updated imports ([#28](https://github.com/aigc-libs/pyopenwebui-python/issues/28)) ([2a5e4fe](https://github.com/aigc-libs/pyopenwebui-python/commit/2a5e4fed5cf03552df2667a3f47105db184e0a27))
* make the `Omit` type public ([#20](https://github.com/aigc-libs/pyopenwebui-python/issues/20)) ([a699cbe](https://github.com/aigc-libs/pyopenwebui-python/commit/a699cbedd59f464afa6395792cd1d26975aee419))
* rebuild project due to codegen change ([#10](https://github.com/aigc-libs/pyopenwebui-python/issues/10)) ([c25250e](https://github.com/aigc-libs/pyopenwebui-python/commit/c25250ec15e6d900e5def60446a9516711d06927))
* rebuild project due to codegen change ([#11](https://github.com/aigc-libs/pyopenwebui-python/issues/11)) ([4d0620f](https://github.com/aigc-libs/pyopenwebui-python/commit/4d0620f84f23c3bcf8e278d3a1f6a50e777416c5))
* rebuild project due to codegen change ([#12](https://github.com/aigc-libs/pyopenwebui-python/issues/12)) ([8382297](https://github.com/aigc-libs/pyopenwebui-python/commit/8382297cb61011baac8d7841f2debf0a081dcf77))
* rebuild project due to codegen change ([#6](https://github.com/aigc-libs/pyopenwebui-python/issues/6)) ([50ba84d](https://github.com/aigc-libs/pyopenwebui-python/commit/50ba84d5f7ef2bb2fd62cb99ad4d02029466a4fb))
* rebuild project due to codegen change ([#8](https://github.com/aigc-libs/pyopenwebui-python/issues/8)) ([ebd0220](https://github.com/aigc-libs/pyopenwebui-python/commit/ebd02208b387ea4422fb834d16a536e95094daa0))
* rebuild project due to codegen change ([#9](https://github.com/aigc-libs/pyopenwebui-python/issues/9)) ([e064261](https://github.com/aigc-libs/pyopenwebui-python/commit/e064261a1186e0f891beebebc265181283232734))
* remove now unused `cached-property` dep ([#15](https://github.com/aigc-libs/pyopenwebui-python/issues/15)) ([8f2d4c9](https://github.com/aigc-libs/pyopenwebui-python/commit/8f2d4c99c0dbb012b756626b325bcdada61f0af6))


### Documentation

* add info log level to readme ([#14](https://github.com/aigc-libs/pyopenwebui-python/issues/14)) ([07724ce](https://github.com/aigc-libs/pyopenwebui-python/commit/07724ce9525b1e9aca4e6c68f49f7519bd830c45))
* **api.md:** fix return type annotations ([#16](https://github.com/aigc-libs/pyopenwebui-python/issues/16)) ([37df760](https://github.com/aigc-libs/pyopenwebui-python/commit/37df760b27db8a051a29c9c2b840915507c56a19))
* **raw responses:** fix duplicate `the` ([#39](https://github.com/aigc-libs/pyopenwebui-python/issues/39)) ([8dfcb08](https://github.com/aigc-libs/pyopenwebui-python/commit/8dfcb08bb3c9e00738d0664de4eeff787ec0949f))
* **readme:** example snippet for client context manager ([#29](https://github.com/aigc-libs/pyopenwebui-python/issues/29)) ([3ac892d](https://github.com/aigc-libs/pyopenwebui-python/commit/3ac892def0bcf77b3d3aafba19d98755c078bc44))
* **readme:** fix http client proxies example ([#22](https://github.com/aigc-libs/pyopenwebui-python/issues/22)) ([534ea9d](https://github.com/aigc-libs/pyopenwebui-python/commit/534ea9d0e0caf8b68a644a81a14c17808dc6acf2))

## 0.3.21 (2024-09-15)

Full Changelog: [v0.0.1-alpha.0...v0.3.21](https://github.com/aigc-libs/pyopenwebui-python/compare/v0.0.1-alpha.0...v0.3.21)

### Chores

* go live ([#1](https://github.com/aigc-libs/pyopenwebui-python/issues/1)) ([92afbcb](https://github.com/aigc-libs/pyopenwebui-python/commit/92afbcb7df1185b7999d4f8577ed85c1911f9e88))
* update SDK settings ([#3](https://github.com/aigc-libs/pyopenwebui-python/issues/3)) ([e8c18d1](https://github.com/aigc-libs/pyopenwebui-python/commit/e8c18d1be937313807521e95759bbab3fefac518))
