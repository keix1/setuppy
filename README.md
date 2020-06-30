# setuppy

setuptoolsを使ってsetup.pyを試してみたリポジトリです。

## 自作モジュールについて

- 今までは頑張って`sys.path.append()`で自作モジュールをimportしていたが、相対パスを考えたりしなくてはならず面倒だった。
- setuptoolsならモジュールを一発入魂できる。
- PyPIにアップロードしてpip installもできる
- GitHubからもpip installできる

## Local develop

### Install on Local develop

ローカルファイルを更新すると即座に更新が反映される。

```sh
cd sample_project
python setup.py develop
```

確認

```sh
pip list | grep sampleA
```

開発用途ならこれで良さそう。

### developインストールするなら下記は省いても動いた

- `__init__.py`
- `setup.py`の下記package部分
```python
packages=find_packages(where='src'), 
package_dir={'': 'src'}
```

### Uninstall on Local develop

```
python setup.py develop -u
```

## pip

上記で触れた`__init__.py`と`setup.py`のpackage記述がいる模様

### pip install

```
cd sample_project
pip install .
```

### pip uninstall

```
pip uninstall SampleA
```

## わかったこと

develop installでは`.egg-info`に関係性が保存されてる様子

## 参考

- [Python 自作モジュールのパッケージ化](https://gist.github.com/3panda/7508508a89bd1ea1990217142eaf3c9c)
- [Python: Twine を使って PyPI にパッケージをアップロードする](https://blog.amedama.jp/entry/2017/12/31/175036)
