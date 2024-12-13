from tortoise import fields, models


class BaseOrmModel(models.Model):
    id = fields.IntField(pk=True, description="id")
    create_datetime = fields.DatetimeField(auto_now_add=True, description="创建时间")
    update_datetime = fields.DatetimeField(auto_now=True, description="更新时间")
    is_del = fields.SmallIntField(default=0, description="是否删除")

    class PydanticMeta:
        exclude = set()
        PydanticMeta= set()

    class Meta:
        abstract = True
