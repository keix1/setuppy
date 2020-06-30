# setuppy

setuptoolsを使ってsetup.pyを試してみたリポジトリです。

## setuptoolsについて

- 今までは頑張って`sys.path.append()`で自作モジュールをimportしていたが、相対パスを考えたりしなくてはならず面倒だった
- setuptoolsなら自作モジュールをpipや開発環境に一発入魂できる
    - どこからでもimportできる
- GitHubからもpip installできる
- コマンドラインツールもinstallできる
- twineを使えばPyPIにアップロードして普通にpip installもできるようになる

## 本レポのディレクトリ構造

```
.
├── setup.py
├── sample
│   ├── __init__.py
│   ├── hoge.py
│   └── sample.py
└── test
    └── test.py
```

## Local develop

- ローカルファイルを更新すると即座に更新が反映される。
- 開発用途ならこれで良さそう。

### Install on Local develop

インストール

```sh
cd setuppy
python setup.py develop
```

確認

```sh
pip list | grep sampleA
```

実行

```sh
python test/test.py
```

### developインストールするなら下記は省いても動いた

- `__init__.py`
- `setup.py`のpackagesとentry_points部分

### Uninstall on Local develop

```sh
python setup.py develop -u
```

## pip

- GitHubに置けばGitHubから配布が可能になる
- 当然だがスクリプトを更新したら再度pip installする必要がある
- 上記で触れた`__init__.py`と`setup.py`のpackage記述がいる

### pip install

```sh
cd setuppy
pip install .
```

### pip install from GitHub

```sh
pip install git+https://github.com/keix1/setuppy.git
```

### pip uninstall

```sh
pip uninstall SampleA
```

## コマンドラインツールとして使う

- 本レポをInstall済みであれば`sample_command`が使えるようになっている

```sh
sample_command
```

- `setup.py`の`entry_points`の`console_scripts`がCLIツール指定するための記述になっている

## わかったこと

- develop installでは`.egg-info`に関係性が保存されてる様子
- `__init__.py`は空ファイルでもいいみたい
- CLIツールとして使えるのちょっとやばい

## 参考

- [Python 自作モジュールのパッケージ化](https://gist.github.com/3panda/7508508a89bd1ea1990217142eaf3c9c)
- [Python: Twine を使って PyPI にパッケージをアップロードする](https://blog.amedama.jp/entry/2017/12/31/175036)
- [Pythonで作ったコマンドをGitHub経由でpipインストール可能にする](https://dev.classmethod.jp/articles/pip-install-via-github-command/)
