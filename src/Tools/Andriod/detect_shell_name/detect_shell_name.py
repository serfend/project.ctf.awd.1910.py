#!/usr/bin/env python3
# coding=utf-8
# python version 3.10 by serfend
#
import sys
import zipfile
import json
import base64
import zlib

config = b'c$|G!Ym@Oz6#Ok)i*l({S%jz{uE|6M2_}~h$XIb(cd~@|?e8Qk_SxO{8_CR>KHYtK@;+xqbBz!!p0`f^JaV#JqJY|xge<^I$|4Et%3@(c-s*3s8u8f)Lx~l8MzNb~DT{DKMATF)SJ?NGf-Jq$P#AUCVzbrb1zA$E3LC+G70zqQ9PJ&3=i_6o&~AL@9JuMl88sKA`<1TKU%3V5YUWZpp_G|P8UEE4!fi1`{_|EZmrJMnGlT(UDtb6PkD*pST}ARfsubjGQsBunOtz17tPY!zqft<MiK5E1`Wr>GqpZ7kp)!&Pm32&;;2l<Tu;HijV3q$o7D>$^Q7T-DYkoC2EI2dz;C4<A4k<;#{ni$E$F>2tmXG(awEHlv;?v#^Ak?Wf`9eo7w~s_l<Q3g+xrY}p`qrE5w<a^pS~jWX@|*cnsU0;9s<~m*hG!~LKt^};soU|F)f1MCIGdx_X17|QV}%AAT1*39(BPXoyF^cwl|?R;m8$Joa}Vp!NauW4Bb<ZrRKOGszgGZh;m(_~ysXYB&Gj31vd_vgz=|jh27+;D6yj{y&X#nW9Lhf^ru`vMj?`zk=`McZ2th!VqoZOpPEW5b=sBTn1ZpIJrwdBzdJM{Xc~SDKAv8qyK4N<Kn3J!9>VgF-y-}z3%>o>WD61kPEp$$)Iha$RT;fl#Y4k~SnG*K19r--XW=z@w`Y_5Miz-#QagjU%vota8em*IyiNQQ%6fRAEdP923uW#a=6{-P7`=NL4W3d!!T#lH!`0B?Fr+2wMJ9G0ps=C<S%IRx^^41r*&cb%irGA|#JTrcFR(Z9QWjc^TR&*2QQT*Uz!+NxSZ=pL-#X8VaN5;IH)qS=Ub#od?J@e;e6DZXXv~N>ubigpB*z7ECzu~c$vmR?)v3KUb&VWg7Qg0m}>VwxdSYx^KKCT$i<gcd3G@_g?`8*YbV}r6CuLC36OgtQ61T4_`8r|)@7!SOv#rRP)p#a1)vgC^a)GS9`8CqvjpL*D)T1LX+C-*K1r5;ENPe$LcWkM~7MEx<fUrX-&Mwd41p>jjX%ege#Gnh`??@pNv*EqC5vih7-$yCIvcgHv8irS9G%Jg1bWp;2)NS(VBKQdyI4EEtk*hO?b9vyk8)GX1-=w)XkKv_OUZ>T_$cVX-~PRhC<x3VkBQ6csx1B2ZA+$gPa#qnA6PP<nD8W>b!w<;9ha<{$kBpr#n_TiM8Pi!inBTWD8ZB?R8DYSase~UTzhE2E#s5#-oc#a^GW(EgxJbJPK9-<}Ix9{W0eay!Zrg8F8kIlZdSn$H|<A>ZeXS}ZAK#|YJ0ZjTpXGy~2v~ZD%;IU2vi8O)ikuvv|+-1zGne6V|*?l_aZ+?zsVe@Q%%eopYcw<`I_qY%AwwZq1#hbF`A__5`R)<g9OaJ#MSV+N4V{E)c7Q~=Gt85+~QU%Ir{}L^qJaQ=JktN1^J6uwheuniH4_o|>C?;CYMISPBmAAT^nR~C&-o45dr_*;AOB<B@bsJFizz8cCXT8dp-Rb3FGmKOv@!zw^v7wU%s3CtsFM`m)wm7VQnA&fry&=B(;L8>V)*MuWe|hcetzP0>ukp%)38Y=P85eHNeJcT7QTG_>vg^*ituXn1h#P2QseMd`2=FSe3+^3Ihr){@{JxG(__+zo;Ja}UTexp6D5OpmKpn{y{!46Fa~@g!d%OHns-Ptkra}YByl4C27WG%mg`NA0fa^j+;FakwblzzC<N|ei>{W5UUm90l_Ln5#5&>?!JZYX@{84Hh_qMr1SHn^q6Bt2MaP{@wtoJ*DJ)1QWIzA((bCE&i@bt-qefs)4p#KSO<}ZAdQDhC_n!74}8vN0!Kj_^v%EXdzZb&$YT~yq=SnA=$aRI2z$A38uP45'
config = base64.b85decode(config)
config = zlib.decompress(config)
config = base64.b85decode(config)
config = json.loads(config.decode())
rules_config = config['rules']
m = {}


def init():
    def add_single(file: str, key: str) -> None:
        if not file in m:
            m[file] = []
        m[file].append(key)

    v = rules_config['v1']
    for key in v:
        for file in v[key]:
            add_single(file, key)


def check(filename: str) -> any:
    file = zipfile.ZipFile(filename)
    result = []
    for f in file.namelist():
        for k in m:
            if k in f:
                result.append([f, m[k]])
    return result


def main(filename: str) -> any:  # list[str]
    result = check(filename)
    if not result:
        print('no shell is found.')
        return
    print('following shell is found:')
    for r in result:
        print(f'{r[0]}:{" | ".join(r[1])}')


if __name__ == '__main__':
    print(f'{config["banner"]}\n{"-"*30}')

    if len(sys.argv) < 2:
        print(f'Example: python {sys.argv[0]} target.apk')
        sys.exit(0)
    f = sys.argv[1]
    init()
    main(f)
