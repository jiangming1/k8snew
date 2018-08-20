from django.db import models
from datetime import datetime

from django.contrib.auth.models import AbstractUser


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class AssetProject(models.Model):
    projects = models.CharField(max_length=128, verbose_name='资产项目')
    ps = models.CharField(max_length=1024, verbose_name="备注", null=True, blank=True)

    class Meta:
        db_table = "AssetProject"
        verbose_name = "资产项目"
        verbose_name_plural = '资产项目'
        permissions = {
            ('read_assetproject', u"只读资产项目"),
            ('cmd_assetproject', u"执行资产项目"),
        }

    def __str__(self):
        return self.projects


class RunDocker(models.Model):
    Name = models.CharField(verbose_name=u"名称",max_length=200)
    Number = models.CharField(verbose_name=u"数量",max_length=200)
    env = models.CharField(verbose_name=u"环境变量",max_length=200)
    readiness = models.CharField(verbose_name=u"readiness",max_length=200)
    liveness = models.CharField(verbose_name=u"liveness",max_length=200)
    images = models.CharField(verbose_name=u"images",max_length=200)

    class Meta:
        verbose_name = u"创建pod"
        verbose_name_plural = verbose_name


class Project(models.Model):
    ip = models.CharField(verbose_name=u"名称",max_length=200)
    ji_fang_dian_hua = models.CharField(verbose_name=u"docker镜像",max_length=200)
    ke_hu_jing_li = models.CharField(verbose_name=u"数量",max_length=200)
    env = models.CharField(verbose_name=u"环境变量",max_length=200)
    readiness = models.CharField(verbose_name=u"readiness",max_length=200)
    liveness = models.CharField(verbose_name=u"liveness",max_length=200)
    bei_zhu_xin_xi = models.CharField(verbose_name=u"备注信息",max_length=200)

    class Meta:
        verbose_name = u"创建pod"
        verbose_name_plural = verbose_name


class Ingress(models.Model):
    ip = models.CharField(verbose_name=u"名称",max_length=200)
    ji_fang_dian_hua = models.CharField(verbose_name=u"docker镜像",max_length=200)
    ke_hu_jing_li = models.CharField(verbose_name=u"数量",max_length=200)
    env = models.CharField(verbose_name=u"环境变量",max_length=200)
    readiness = models.CharField(verbose_name=u"readiness",max_length=200)
    liveness = models.CharField(verbose_name=u"liveness",max_length=200)
    bei_zhu_xin_xi = models.CharField(verbose_name=u"备注信息",max_length=200)

    class Meta:
        verbose_name = u"创建pod"
        verbose_name_plural = verbose_name


class Pod(models.Model):
    ip = models.CharField(verbose_name=u"名称",max_length=200)
    ji_fang_dian_hua = models.CharField(verbose_name=u"docker镜像",max_length=200)
    ke_hu_jing_li = models.CharField(verbose_name=u"数量",max_length=200)
    env = models.CharField(verbose_name=u"环境变量",max_length=200)
    readiness = models.CharField(verbose_name=u"readiness",max_length=200)
    liveness = models.CharField(verbose_name=u"liveness",max_length=200)
    bei_zhu_xin_xi = models.CharField(verbose_name=u"备注信息",max_length=200)

    class Meta:
        verbose_name = u"创建pod"
        verbose_name_plural = verbose_name


class Service(models.Model):
    ip = models.CharField(verbose_name=u"名称",max_length=200)
    ji_fang_dian_hua = models.CharField(verbose_name=u"docker镜像",max_length=200)
    ke_hu_jing_li = models.CharField(verbose_name=u"数量",max_length=200)
    env = models.CharField(verbose_name=u"环境变量",max_length=200)
    readiness = models.CharField(verbose_name=u"readiness",max_length=200)
    liveness = models.CharField(verbose_name=u"liveness",max_length=200)
    bei_zhu_xin_xi = models.CharField(verbose_name=u"备注信息",max_length=200)

    class Meta:
        verbose_name = u"创建服务"
        verbose_name_plural = verbose_name



class ZhuJiip(models.Model):
    ip = models.CharField(verbose_name=u"机房地址",max_length=200)
    ji_fang_dian_hua = models.CharField(verbose_name=u"机房电话",max_length=200)
    ke_hu_jing_li = models.CharField(verbose_name=u"客户经理",max_length=200)
    yi_dong_dian_hua = models.CharField(verbose_name=u"移动电话",max_length=200)
    ji_gui_xin_xi = models.CharField(verbose_name=u"机柜信息",max_length=200)
    jie_ru_dai_kuan = models.CharField(verbose_name=u"接入带宽",max_length=200)
    bei_zhu_xin_xi = models.CharField(verbose_name=u"备注信息",max_length=200)

    class Meta:
        verbose_name = u"高防ip"
        verbose_name_plural = verbose_name


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class Dns(models.Model):

    name = models.CharField(verbose_name=u"域名", max_length=200)
    bei_zhu = models.CharField(verbose_name=u"备注", max_length=200)

    class Meta:
        verbose_name = u"域名"
        verbose_name_plural = verbose_name
    def __str__(self):
        return '{0}'.format(self.name)

class DnsIp(models.Model):
    yu_ming = models.ForeignKey(Dns, on_delete=models.CASCADE, verbose_name=u"域名")
    zhu_ji_ji_lu = models.CharField(verbose_name="主机记录", max_length=200)
    ji_lu_zhi = models.CharField(verbose_name=u"记录值",max_length=200)
    ip = models.CharField(verbose_name=u"ip",max_length=200)

    class Meta:
        verbose_name = u"负责人管理"
        verbose_name_plural = verbose_name



class JiFangGuanLi(models.Model):
    ji_fang_biao_shi = models.CharField(verbose_name=u"机房标识",max_length=200)
    ji_fang_ming_chen = models.CharField(verbose_name=u"机房名称",max_length=200)
    ji_fang_di_zhi = models.CharField(verbose_name=u"机房地址",max_length=200)
    ji_fang_dian_hua = models.CharField(verbose_name=u"机房电话",max_length=200)
    ke_hu_jing_li = models.CharField(verbose_name=u"客户经理",max_length=200)
    yi_dong_dian_hua = models.CharField(verbose_name=u"移动电话",max_length=200)
    ji_gui_xin_xi = models.CharField(verbose_name=u"机柜信息",max_length=200)
    jie_ru_dai_kuan = models.CharField(verbose_name=u"接入带宽",max_length=200)
    bei_zhu_xin_xi = models.CharField(verbose_name=u"备注信息",max_length=200)

    class Meta:
        verbose_name = u"机房管理"
        verbose_name_plural = verbose_name


class ShuZuGuanLi(models.Model):
    fu_wu_qi_zu = models.CharField(verbose_name=u"服务器组",max_length=200)
    miao_su = models.CharField(verbose_name=u"描述",max_length=200)
    ke_xuan_fu_wu_qi = models.CharField(verbose_name=u"可选择服务器",max_length=200)

    class Meta:
        verbose_name = u"机房管理"
        verbose_name_plural = verbose_name


class ZhuJiGuanLi(models.Model):
    yu_ming = models.ForeignKey(Dns, on_delete=models.CASCADE, verbose_name=u"域名")
    zu_ji_ming = models.CharField(verbose_name=u"主机名",max_length=200)
    guan_li_ip = models.CharField(verbose_name=u"管理ip",max_length=200)
    suo_zai_ji_fang = models.CharField(verbose_name=u"所在机房",max_length=200)
    qi_ta_ip = models.CharField(verbose_name=u"其他ip",max_length=200)
    zi_can = models.CharField(verbose_name=u"资产",max_length=200)
    she_bei_lei_xing = models.CharField(verbose_name=u"设备类型",max_length=200)
    she_bei_zhuang_tai = models.CharField(verbose_name=u"设备状态",max_length=200)
    cao_zuo_xi_tong = models.CharField(verbose_name=u"操作系统",max_length=200)
    she_bei_chang_shang = models.CharField(verbose_name=u"设备厂商",max_length=200)
    shang_jia_shi_jian = models.CharField(verbose_name=u"上架时间",max_length=200)
    cpu_xing_hao = models.CharField(verbose_name=u"CPU型号",max_length=200)
    cpu_shu_liang = models.CharField(verbose_name=u"cpu数量",max_length=200)
    nei_cun_da_xiao = models.CharField(verbose_name=u"内存大小",max_length=200)
    ying_pan_xin_xi = models.CharField(verbose_name=u"硬盘信息",max_length=200)
    SN_hao_ma = models.CharField(verbose_name=u"SN号码",max_length=200)
    suo_zai_wei_zhi = models.CharField(verbose_name=u"所在位置",max_length=200)
    bei_zhu_xin_xi = models.CharField(verbose_name=u"备注信息",max_length=200)

    class Meta:
        verbose_name = u"主机管理"
        verbose_name_plural = verbose_name



class ChanPinGuanLi(models.Model):
    can_pin_ming_chen = models.CharField(verbose_name=u"产品名称",max_length=200)
    can_pin_miao_shu = models.CharField(verbose_name=u"产品描述",max_length=200)
    can_pin_fu_ze_ren = models.CharField(verbose_name=u"产品负责人",max_length=200)

    class Meta:
        verbose_name = u"产品管理"
        verbose_name_plural = verbose_name


class XiangMuGuanLi(models.Model):
    xiang_mu_ming_chen = models.CharField(verbose_name=u"项目名称",max_length=200)
    xiang_mu_miao_su = models.CharField(verbose_name=u"项目描述",max_length=200)
    yu_yan_lei_xing = models.CharField(verbose_name=u"语言类型",max_length=200)
    cheng_xu_lei_xing = models.CharField(verbose_name=u"程序类型",max_length=200)
    fu_wu_qi_lei_xing = models.CharField(verbose_name=u"服务器类型",max_length=200)
    yuan_lei_xing = models.CharField(verbose_name=u"源类型",max_length=200)
    yuan_di_zhi = models.CharField(verbose_name=u"源地址",max_length=200)
    cheng_xu_bu_shu_lu_jing = models.CharField(verbose_name=u"程序部署路径",max_length=200)
    pei_zhi_wen_jian = models.CharField(verbose_name=u"配置文件路径",max_length=200)
    suo_su_chan_pin = models.CharField(verbose_name=u"所属产品",max_length=200)
    xiang_mu_fu_ze_ren = models.CharField(verbose_name=u"项目负责人",max_length=200)
    suo_zai_fu_wu_qi = models.CharField(verbose_name=u"所在服务器",max_length=200)

    class Meta:
        verbose_name = u"项目管理"
        verbose_name_plural = verbose_name


class FuZeRen(models.Model):
    fu_ze_ren = models.CharField(verbose_name=u"负责人姓名",max_length=200)
    shou_ji = models.CharField(verbose_name=u"负责人手机",max_length=200)
    qq = models.CharField(verbose_name=u"负责人qq",max_length=200)
    wechat = models.CharField(verbose_name=u"负责人微信",max_length=200)

    class Meta:
        verbose_name = u"负责人管理"
        verbose_name_plural = verbose_name


class ChiXuJiaoFu(models.Model):
    xiang_mu_ming = models.CharField(verbose_name=u"项目名",max_length=200)
    xiang_mu_miaosu = models.CharField(verbose_name=u"项目描述",max_length=200)
    ban_ben_xin_xi = models.CharField(verbose_name=u"版本信息",max_length=200)
    shell = models.CharField(verbose_name=u"shell",max_length=200)

    class Meta:
        verbose_name = u"持续交付"
        verbose_name_plural = verbose_name


class JiZhangYuan(models.Model):
    ji_zhang_yuan = models.CharField(verbose_name=u"供商名称",max_length=200)

    class Meta:
        verbose_name = u"记账员"
        verbose_name_plural = verbose_name


class GuanKuYuan(models.Model):
    guan_ku_yuan = models.CharField(verbose_name=u"供商名称",max_length=200)

    class Meta:
        verbose_name = u"记账员"
        verbose_name_plural = verbose_name


class GongShangXinXi(models.Model):
    gong_shang_ming_chen = models.CharField(verbose_name=u"供商名称",max_length=200)
    lian_xi_ren =  models.CharField(verbose_name=u"联系人",max_length=200)
    lian_xi_dian_hua =  models.CharField(verbose_name=u"联系电话",max_length=200)
    lian_xi_di_zhi =  models.CharField(verbose_name=u"联系地址",max_length=200)
    bei_zhu =  models.CharField(verbose_name=u"备注",max_length=200)

    class Meta:
        verbose_name = u"供应商信息"
        verbose_name_plural = verbose_name


class ShuiNiXinXi(models.Model):
    shui_ni_bian_hao = models.CharField(verbose_name=u"水泥编号", max_length=200)
    chang_jia = models.CharField(verbose_name=u"厂家", max_length=200)
    pin_pai = models.CharField(verbose_name=u"品牌", max_length=200)
    xing_hao = models.CharField(verbose_name=u"型号", max_length=200)
    gui_ge = models.CharField(verbose_name=u"规格", max_length=200)
    bei_zhu = models.CharField(verbose_name=u"备注", max_length=200)

    class Meta:
        verbose_name = u"水泥信息"
        verbose_name_plural = verbose_name


class KeHuXinXi(models.Model):
    ke_hu_bian_hao = models.CharField(blank=True, verbose_name=u"客户编号", max_length=200)
    qu_yu = models.CharField(verbose_name=u"区域", max_length=200)
    ke_hu_ming_chen = models.CharField(verbose_name=u"客户名称", max_length=200)
    fu_ze_ren = models.CharField(verbose_name=u"负责人", max_length=200)
    fu_ze_dian_hua = models.CharField(verbose_name=u"负责电话", max_length=200)
    tiao_liao_yuan = models.CharField(verbose_name=u"调料员", max_length=200)
    dian_hua = models.CharField(verbose_name=u"电话", max_length=200)
    di_zhi = models.CharField(verbose_name=u"地址", max_length=200)
    ye_wu = models.CharField(verbose_name=u"业务", max_length=200)
    xin_yong_e_du = models.CharField(verbose_name=u"信用额度", max_length=200)
    bei_zhu = models.CharField(verbose_name=u"备注", max_length=200)

    class Meta:
        verbose_name = u"客户信息"
        verbose_name_plural = verbose_name


class ZhuangXieGong(models.Model):
    zhuang_xie_gong = models.CharField(verbose_name=u"装卸工", max_length=200)
    dianhua1 = models.CharField(verbose_name=u"联系电话1", max_length=200)
    dianhua2 = models.CharField(verbose_name=u"联系电话2", max_length=200)
    bei_zhu = models.CharField(verbose_name=u"备注", max_length=200)

    class Meta:
        verbose_name = u"装卸工信息"
        verbose_name_plural = verbose_name


class DanWei(models.Model):
    dan_wei_ming_cheng = models.CharField(verbose_name=u"单位名称", max_length=200)
    lian_xi_ren = models.CharField(verbose_name=u"联系人", max_length=200)
    lian_xi_dian_hua = models.CharField(verbose_name=u"联系电话", max_length=200)
    lian_xi_di_zhi = models.CharField(verbose_name=u"联系地址", max_length=200)
    bei_zhu = models.CharField(verbose_name=u"备注", max_length=200)

    class Meta:
        verbose_name = u"单位信息"
        verbose_name_plural = verbose_name


class CheLiang(models.Model):
    che_hao = models.CharField(verbose_name=u"车号", max_length=200)
    si_ji = models.CharField(verbose_name=u"司机", max_length=200)
    dian_hua1 = models.CharField(verbose_name=u"联系电话1", max_length=200)
    dian_hua2 = models.CharField(verbose_name=u"联系电话2", max_length=200)
    bei_zhu = models.CharField(verbose_name=u"备注", max_length=200)

    class Meta:
        verbose_name = u"车辆信息"
        verbose_name_plural = verbose_name


class CaiGou(models.Model):
    cai_gou_ri_qi = models.CharField(verbose_name=u"采购日期", max_length=200)
    chang_jia = models.CharField(verbose_name=u"厂家", max_length=200)
    chang_ku_ming_cheng = models.CharField(verbose_name=u"仓库名称", max_length=200)
    cai_gou_fang_shi = models.CharField(verbose_name=u"采购方式", max_length=200)
    pin_pai = models.CharField(verbose_name=u"品牌", max_length=200)
    xing_hao = models.CharField(blank=True, verbose_name=u"型号", max_length=200)
    gui_ge = models.CharField(verbose_name=u"规格", max_length=200)
    dan_jia = models.CharField(verbose_name=u"单价", max_length=200)
    shu_liang = models.CharField(verbose_name=u"数量", max_length=200)
    jin_e = models.CharField(verbose_name=u"金额", max_length=200)
    che_chuan_hao = models.CharField(verbose_name=u"车船号", max_length=200)
    yun_jia = models.CharField(verbose_name=u"运价", max_length=200)
    yun_fei = models.CharField(verbose_name=u"运费", max_length=200)
    cao_zuo_yuan = models.CharField(verbose_name=u"操作员", max_length=200)
    bei_zhu = models.CharField(verbose_name=u"备注", max_length=200)


    class Meta:
        verbose_name = u"采购登记"
        verbose_name_plural = verbose_name


class CaiGouSunHao(models.Model):
    ri_qi = models.CharField(verbose_name=u"日期", max_length=200)
    cang_ku_ming_cheng = models.CharField(verbose_name=u"仓库名称", max_length=200)
    cang_jia = models.CharField(verbose_name=u"厂家", max_length=200)
    pin_pai = models.CharField(verbose_name=u"品牌", max_length=200)
    xing_hao = models.CharField(verbose_name=u"型号", max_length=200)
    gui_ge = models.CharField(blank=True, verbose_name=u"规格", max_length=200)
    sun_hao_shu_liang = models.CharField(verbose_name=u"损耗数量", max_length=200)
    cao_zuo_yuan = models.CharField(verbose_name=u"操作员", max_length=200)
    bei_zhu = models.CharField(verbose_name=u"备注", max_length=200)

    class Meta:
        verbose_name = u"采购损耗"
        verbose_name_plural = verbose_name


class XiaoShouDengJi(models.Model):
    dan_hao = models.CharField(verbose_name=u"单号", max_length=200)
    ri_qi = models.CharField(verbose_name=u"日期", max_length=200)
    qu_yu = models.CharField(verbose_name=u"区域", max_length=200)
    ke_hu_ming_cheng = models.CharField(verbose_name=u"客户名称", max_length=200)
    che_pai_hao = models.CharField(verbose_name=u"车牌号", max_length=200)
    si_ji = models.CharField(blank=True, verbose_name=u"司机", max_length=200)
    si_ji_dian_hua = models.CharField(verbose_name=u"司机电话", max_length=200)
    fu_kuan_fang_shi = models.CharField(verbose_name=u"付款方式", max_length=200)
    jin_e = models.CharField(verbose_name=u"金额", max_length=200)
    you_hui_jin_e = models.CharField(verbose_name=u"优惠金额", max_length=200)
    yin_shou_jin_e = models.CharField(verbose_name=u"应收金额", max_length=200)
    shi_shou_jin_e = models.CharField(blank=True, verbose_name=u"实收金额", max_length=200)
    cao_zuo_yuan = models.CharField(verbose_name=u'操作员', max_length=200)
    bei_zhu = models.CharField(verbose_name=u"备注", max_length=200)
    da_yin = models.CharField(verbose_name=u"打印", max_length=200)

    class Meta:
        verbose_name = u"销售登记"
        verbose_name_plural = verbose_name


class SiJiJieSuan(models.Model):
    ri_qi = models.CharField(verbose_name=u"日期", max_length=200)
    che_pai_hao = models.CharField(verbose_name=u"车牌号", max_length=200)
    si_ji_xing_ming = models.CharField(verbose_name=u"司机姓名", max_length=200)
    si_ji_dian_hua = models.CharField(verbose_name=u"司机电话", max_length=200)
    dang_qian_yun_fei = models.CharField(verbose_name=u"当前运费", max_length=200)
    fu_yun_fei = models.CharField(blank=True, verbose_name=u"付运费", max_length=200)
    fu_kuan_fang_shi = models.CharField(verbose_name=u"付款方式", max_length=200)
    wei_fu_yun_fei = models.CharField(verbose_name=u"未付运费", max_length=200)
    cao_zuo_yuan = models.CharField(verbose_name=u'操作员', max_length=200)
    bei_zhu = models.CharField(verbose_name=u"备注", max_length=200)
    da_yin = models.CharField(verbose_name=u"打印", max_length=200)

    class Meta:
        verbose_name = u"司机结算"
        verbose_name_plural = verbose_name



class ZhuangXieJieSuan(models.Model):
    ri_qi = models.CharField(verbose_name=u"日期", max_length=200)
    zhuang_xie_gong = models.CharField(verbose_name=u"装卸工", max_length=200)
    dang_qian_zhuang_xie = models.CharField(verbose_name=u"当前装卸", max_length=200)
    fu_zhuang_xie_fei = models.CharField(verbose_name=u"付装卸费", max_length=200)
    wei_fu_zhuang_xie = models.CharField(verbose_name=u"未付装卸", max_length=200)
    cao_zuo_yuan = models.CharField(verbose_name=u'操作员', max_length=200)
    bei_zhu = models.CharField(verbose_name=u"备注", max_length=200)
    da_yin = models.CharField(verbose_name=u"打印", max_length=200)

    class Meta:
        verbose_name = u"装卸结算"
        verbose_name_plural = verbose_name


class CaiGouYunFeiJieSuan(models.Model):
    ri_qi = models.CharField(verbose_name=u"日期", max_length=200)
    che_chuan_hao = models.CharField(verbose_name=u"车船号", max_length=200)
    dang_qian_yun_fei = models.CharField(verbose_name=u"当前运费", max_length=200)
    jie_suan_yun_fei = models.CharField(verbose_name=u"结算运费", max_length=200)
    cao_zuo_yuan = models.CharField(verbose_name=u"操作员", max_length=200)
    bei_zhu = models.CharField(verbose_name=u"备注", max_length=200)

    class Meta:
        verbose_name = u"采购运费结算"
        verbose_name_plural = verbose_name


class ShuiNi(models.Model):
    ri_qi = models.CharField(verbose_name=u"日期", max_length=200)
    qu_yu = models.CharField(verbose_name=u"区域", max_length=200)
    ke_hu_ming_cheng = models.CharField(verbose_name=u"客户名称", max_length=200)
    wei_fu_huo_kuan = models.CharField(verbose_name=u"未付货款", max_length=200)
    fu_kuan_jin_e = models.CharField(verbose_name=u"付款金额", max_length=200)
    da_xie = models.CharField(verbose_name=u"大写", max_length=200)
    fu_kuan_fang_shi = models.CharField(verbose_name=u"付款方式", max_length=200)
    sheng_yu_huo_kuan = models.CharField(verbose_name=u"剩余货款", max_length=200)
    cao_zuo_yuan = models.CharField(verbose_name=u"操作员", max_length=200)
    da_yin = models.CharField(verbose_name=u"打印", max_length=200)

    class Meta:
        verbose_name = u"水泥货款"
        verbose_name_plural = verbose_name


class CaiGouFuKuan(models.Model):
    ri_qi = models.CharField(verbose_name=u"日期", max_length=200)
    cang_jia = models.CharField(verbose_name=u"厂家", max_length=200)
    qian_kuan_jin_e = models.CharField(verbose_name=u"欠款金额", max_length=200)
    fu_kuan_jin_e = models.CharField(verbose_name=u"付款金额", max_length=200)
    cao_zuo_yuan = models.CharField(verbose_name=u"操作员", max_length=200)
    da_yin = models.CharField(verbose_name=u"打印", max_length=200)

    class Meta:
        verbose_name = u"采购付款"
        verbose_name_plural = verbose_name


class DangQianKuCun(models.Model):
    chang_ku_ming_cheng = models.CharField(verbose_name=u"仓库名称", max_length=200)
    cang_jia = models.CharField(verbose_name=u"厂家", max_length=200)
    pin_pai = models.CharField(verbose_name=u"品牌", max_length=200)
    xing_hao = models.CharField(verbose_name=u"型号", max_length=200)
    gui_ge = models.CharField(verbose_name=u"规格", max_length=200)
    cai_gou_shu_liang = models.CharField(verbose_name=u"采购数量", max_length=200)
    song_huo_shu_liang = models.CharField(verbose_name=u"送货数量", max_length=200)
    sun_hao_shu_liang = models.CharField(verbose_name=u"损耗数量", max_length=200)
    ku_cun_shu_liang = models.CharField(verbose_name=u"库存数量", max_length=200)

    class Meta:
        verbose_name = u"订单库存"
        verbose_name_plural = verbose_name


class UserProfile(AbstractUser):
    # 自定义的性别选择规则
    GENDER_CHOICES = (
        ("male", u"男"),
        ("female", u"女")
    )
    # 昵称
    nick_name = models.CharField(max_length=50, verbose_name=u"昵称", default="")
    # 生日，可以为空
    birthday = models.DateField(verbose_name=u"生日", null=True, blank=True)
    # 性别 只能男或女，默认女
    gender = models.CharField(
        max_length=6,
        verbose_name=u"性别",
        choices=GENDER_CHOICES,
        default="female")
    # 地址
    address = models.CharField(max_length=100, verbose_name="地址", default="")
    # 推荐人
    tuijianren = models.CharField(max_length=100, verbose_name="推荐人", default="")

    # 资金
    cunkuan = models.DecimalField(verbose_name="资金", default=0, max_digits=19, decimal_places=2)
    # 电话
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name=u"电话")
    # 头像 默认使用default.png
    image = models.ImageField(
        upload_to="image/%Y/%m",
        default=u"image/default.png",
        max_length=100,
        verbose_name=u"头像"
    )

    # meta信息，即后台栏目名
    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    # 重载__str__方法，打印实例会打印username，username为继承自AbstractUser
    def __str__(self):
        return self.username

    # 获取用户未读消息的数量
    def unread_nums(self):
        from operation.models import UserMessage
        return  UserMessage.objects.filter(has_read=False, user=self.id).count()


# 邮箱验证码model


class EmailVerifyRecord(models.Model):
    SEND_CHOICES = (
        ("register", u"注册"),
        ("forget", u"找回密码"),
        ("update_email", u"修改邮箱"),
    )
    code = models.CharField(max_length=20, verbose_name=u"验证码")
    # 未设置null = true blank = true 默认不可为空
    email = models.EmailField(max_length=50, verbose_name=u"邮箱")
    send_type = models.CharField(choices=SEND_CHOICES, max_length=20, verbose_name=u"验证码类型")
    # 这里的now得去掉(),不去掉会根据编译时间。而不是根据实例化时间。
    send_time = models.DateTimeField(default=datetime.now, verbose_name=u"发送时间")

    class Meta:
        verbose_name = "邮箱验证码"
        verbose_name_plural = verbose_name


    # 重载str方法使后台不再直接显示object
    def __str__(self):
        return '{0}({1})'.format(self.code, self.email)


# 轮播图model
class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name=u"标题")
    image = models.ImageField(
        upload_to="banner/%Y/%m",
        verbose_name=u"轮播图",
        max_length=100)
    url = models.URLField(max_length=200, verbose_name=u"访问地址")
    # 默认index很大靠后。想要靠前修改index值。
    index = models.IntegerField(default=100, verbose_name=u"顺序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"轮播图"
        verbose_name_plural = verbose_name


    # 重载__str__方法使后台不再直接显示object
    def __str__(self):
        return '{0}(位于第{1}位)'.format(self.title, self.index)