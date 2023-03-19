# なにこれ

perl の CGI で Discord のいろいろを取得する何か

# 使い方

1. config.cgi.default を config.cgi にリネーム
2. config.cgi の5つの値に適切な値を入れる。
  * `$APPLICATION_PASSWORD` 任意の文字列。 perl にリクエストを送るためのパスワード
  * `$DISCORD_TOKEN` Discord にアクセスするための Bot の Token
  * `$WORKING_URL` Discord にアクセスする際に送る、アプリが動いているサーバの情報
  * `$DISCORD_API_VERSION` Discord の API のバージョン
  * `$DISCORD_GUILD_ID` アクティブなスレッドを拾う対象とするサーバの ID
3. config.cgi だけ 644 のパーミッションで、他は 755 のパーミッションでサーバに配置する
4. curl でリクエストする。例えば以下のような感じ

```bash
curl -H "X-Auth-Token: $APPLICATION_PASSWORDの値" https://配置したファイルのパス/channels.cgi
```
