## Welcome To Dapunta API

This repository contains a collection  
of APIs that can be accessed for free  

> Author :  
> -> [**Dapunta Khurayra X**](https://www.facebook.com/Dapunta.Khurayra.X)  
> -> **DyrtEastStar**  

check it on [`https://api.dapuntaratya.com`](https://api.dapuntaratya.com)

## List API

### Facebook

url : [`https://api.dapuntaratya.com/facebook-api`](https://api.dapuntaratya.com/facebook-api)

| Edges   | Payload |
| :------ | :------ |
| [/login](https://api.dapuntaratya.com/facebook-api/login)     | `cookie` or `email`, `password` |
| [/token](https://api.dapuntaratya.com/facebook-api/token)     | `cookie`, `type`                |
| [/post](https://api.dapuntaratya.com/facebook-api/post)       | `cookie`, `token`               |
| [/react](https://api.dapuntaratya.com/facebook-api/react)     | `cookie`, `token`, `post`       |
| [/privacy](https://api.dapuntaratya.com/facebook-api/privacy) | `cookie`, `post`, `privacy`     |

| Payload  | Description | Type | Example |
| :------- | :---------- | :--- | :------ |
| `cookie`   | facebook account cookies      | string | datr=abcd;c_user=4;sb=efgh... |
| `token`    | facebook account access token | string | EAAGdApUnTaHaNdSoMe.......    |
| `type`     | type of facebook access token | string | EAAG                          |
| `email`    | facebook account email        | string | root@dapuntaratya.com         |
| `password` | facebook account password     | string | r0ots3c$@#                    |
| `post`     | facebook post id              | string | [10214228940637251](https://www.facebook.com/photo/?fbid=10214228940637251&set=a.1274773809249) |
| `privacy`  | destination privacy option    | string | SELF |

> Note :  
> -> `type` only available in `EAAG`, `EAAB`, `EAAD`, `EAAC`, `EAAF`, and `EABB`  
> -> `privacy` only available in `SELF`, `FRIENDS`, and `EVERYONE`

### Terabox

url : [`https://api.dapuntaratya.com/terabox-api`](https://api.dapuntaratya.com/terabox-api)

| Edges | Payload |
| :---- | :------ |
| [/fetch](https://api.dapuntaratya.com/terabox-api/fetch) | `url` |

| Payload | Description | Type | Example |
| :------ | :---------- | :--- | :------ |
| `url`   | terabox source url | string | https://terabox.com/s/1x_bUro1EoMkWfb1eX-zwtQ |

## Support

Happy Hacking ;)