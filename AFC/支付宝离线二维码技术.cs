支付宝离线二维码技术标准

        手机客户端  这里特指安装在手机上的应用本规范二维码应用的软件。【eg：西安地铁APP】

        二维码票卡  特指通过【二维码为载体】发行的电子票卡，主要在形态上区别于实体票卡

        票卡二维码  特指二维码票卡产生的【二维码图案】

        二维码发行机构  特指【发行离线二维码机构】【eg：西安地铁目前是支付宝，后期是app】

        票卡发行机构  特指【发行二维码票卡的机构】【eg：西安地铁】

        公私密钥对  【非对称密钥中】的【公钥和私钥】

        私钥  Private Key，非对称密钥对中，非公开的密钥

        公钥  Public Key，非对称密钥对中，公开的密钥

        受理终端  Terminal，这里指【能支持识别和受理本规范二维码的终端设备】 --【eg：西安地铁中的闸机，读头】

        二维码受理记录  指【受理】终端受理票卡二维码【后】【根据本规范】【生成的记录数据】


  票卡发行 机构：二维码票卡发行机构，向使用二维码票卡业务的用户发行二维码票卡，例如公
交卡、校园卡、市民卡等发卡机构；票卡发行机构负责发行、运营和管理用户票卡；

  二维码发行机构：为二维码票卡发行二维码，可以是票卡发行机构本身，也可以是用户、票卡
发行机构共同信任的可信第三方，例如支付宝、银联等支付机构；二维码发行机构负责认证
用户身份，进行二维码的发行和管理，确保二维码的安全性；


1) 票卡发行机构向用户发行二维码票卡，票卡发行机构可根据业务规则生成二维码票卡数据，对
于票卡数据有机密性要求时，票卡发行机构可以对生成的票卡数据进行安全加密；

2) 票卡发行机构将二维码票卡数据发送给二维码发行机构，由二维码发行机构进行授权；

3) 二维码发行机构验证用户资质，使用【机构私钥】对二维码票卡数据进行签名授权；其中，签名是
通过二维码发行机构的【私钥】产生，【发码机构授权数据】不可伪造且不可否认；

4) 用户使用二维码票卡时，使用【用户私钥】对【时间戳】和【二维码发行机构的授权数据】进行【签名】；时间
戳控制生成的【二维码有效时间范围】，【提高二维码复制泄露的难度和风险】；签名通过用户私钥
产生，用户使用数据不可伪造且不可否认；

5) 受理终端使用【发码机构公钥】【验证】【发码机构签名合法性】，再使用【二维码中】【用户公钥验证用户签名
合法性】，根据【发码时间戳验证二维码有效性】；对【有效的二维码提取原始票卡数据，根据受理
终端与票卡发行机构约定的验证逻辑验证票卡数据有效性】；【票卡数据需要加密时，受理终端
与票卡发行机构约定验证方法，包括加密算法、密钥规则等】；

6) 受理终端受理票卡二维码后【根据业务规则】选择进行【脱机交易或联机交易】；

支付宝授权------机构私钥签名进行票卡数据授权
            
            ---获取票卡授权数据
            
            ---用户私钥签名进行使用授权
            
            ---生成票卡二维码
            
            【刷码进站】

            ---扫码识别

            ---闸机端有发吗机构的公钥，公钥验证票卡数据授权的合法性

            ---用户公钥验证用户签名授权合法性

            ---验证票卡数据的合法性

            ---生成二维码受理记录

                ---联机/脱机交易
                    --请求扣款（请款）
                        --支付

        概念：用户公钥，用户私钥，码发行机构公钥



        二维码协议格式
            协议头
                协议头部

                    【二维码版本】  1字节 定义二维码协议版本

                    【算法版本】    1字节 定义二维码安全算法版本

                    【密钥ID】     1字节 定义二维码发行机构授权数据签名密钥编号

            
            机构授权数据

                    【长度】    1字节   机构授权数据长度 

                    【用户ID】  16字节  使用二维码的用户ID 

                    【过期时间】  4字节  机构授权数据有效时间，过期无效使用UTC(0时区)时间1970年1月1日00:00:00到现在的秒数

                    【二维码有效时长】  2字节  二维码生成后的有效时长，过期无效单位秒

                    【限额】  2字节  二维码允许的单笔交易限额 单位分

                    【用户身份】  4字节  表示特定用户的身份-----------------例如学生身份

                    【机构编码】  4字节  唯一确定二维码发行机构------------二维码发行机构编码可向支付宝申请

                    【保留字段】  4字节  -  保留

                    【用户公钥】  不定  用户密钥对中的公钥-------------密钥长度和算法由协议头部算法版本确定

                    【票卡类型】  8字节  二维码代表的票卡类型--------------------票卡发行机构与二维码发行机构约定

                    【票卡编号长度】  1字节  票卡编号的长度 

                    【票卡编号】  不定  票卡号码 

                    【票卡数据长度】  1字节  票卡数据长度 

                    【票卡数据】  不定  票卡数据---------------------------票卡发行机构自定义， 数据可加密；无票卡数据时为空；

                    【授权数据签名长度】  1字节  授权数据签名的长度 

                    【授权数据签名】  不定  二维码发行机构私钥对授权数据签名结果-----------签名算法由协议头部协议版本确定

            用户授权数据

                    【长度】  1字节  用户授权数据长度

                    【生码时间】  4字节  二维码的生成时间  使用UTC(0时区)时间1970年1月1日00:00:00到现在的秒数

                    【用户签名长度】  1字节  用户签名的长度 

                    【用户签名】  不定长  用户私钥签名结果 








    受理记录协议
        受理记录协议版本
            头部信息

                【受理记录协议版本】  4比特  受理记录协议版本 

                【受理记录长度】  12比特  受理记录长度

        二维码长度
            二维码信息

                【二维码长度】  2字节  原始二维码信息长度 

                【二维码】  不定长  原始二维码数据  二维码数据格式见二维码协议部分

        受理终端信息长度
            受理终端信息

                【受理终端ID】  不定长  受理终端ID，唯一表示受理终端

                【受理记录类型】  不定长  区分联机、脱机等交易类型

                【受理记录名称】  不定长  描述本次票卡受理业务 

                【受理记录ID】  不定长  受理记录唯一单据号

        受理时间长度
            受理时间

                【受理时间长度】  2字节  受理时间的长度 

                【受理时间】  4字节  受理记录的时间戳  使用UTC(0时区)时间1970年1月1日00:00:00到现在的秒数

        完整性签名长度
            完整性签名

                【完整性签名长度】  2字节  完整性签名长度 

                【完整性签名】  不定长  受理记录完整性签名  算法由受理终端与支付机构约定

        
        机构私钥：【二维码发行机构】-KMI或加密机

        机构公钥：【二维码发行机构】-可明文存储，【受理终端】-可明文存储

        用户私钥：【二维码发行机构】-KMI或加密机，【手机客户端】-手机安全存储区，例如TEE,黑匣子

        用户公钥：【二维码发行机构】-可明文存储，【手机客户端】-可明文存储

        机构授权数据：【手机客户端】-可明文存储

        二维码受理记录：【受理终端】-可明文存储，需放篡改



机构授权数据  机构私钥签名  不可仿造、不可抵赖

票卡二维码  用户私钥签名  不可仿造、不可抵赖

主体间请求应答报文   主体证书签名  不可伪造，不可抵赖


手机端-请码-用户私钥（签名），用户公钥（可能需要），码发行机构私钥（签名）----扫码---闸机码发行机构公钥