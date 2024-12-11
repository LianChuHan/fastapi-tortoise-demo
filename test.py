from pydantic import BaseModel, Field, model_serializer, model_validator, field_validator, field_serializer


class User(BaseModel):
    name: str
    age: int

    @model_validator(mode="wrap")
    @classmethod
    def validate_wrap(cls, values, handler, info):
        print("model_validator-->wrap")
        print(handler(values))

        return  handler(values)
    @model_validator(mode="before")
    @classmethod
    def validate_before(cls, values):
        print("model_validator-->before")
        print(values)
        return values

    @model_validator(mode="after")
    @classmethod
    def validate_after(cls, model):
        print("model_validator-->after")
        print(model)
        return model

    @field_validator("name", mode="before")
    @classmethod
    def set_name_before(cls, value):
        print("field_validator->before")
        new_name = value + 'bbb'
        print(new_name)
        return new_name

    @field_validator("name", mode="after")
    @classmethod
    def set_name_after(cls, value):
        print("field_validator->after")
        new_name = value + 'aaa'
        print(new_name)
        return new_name

    @field_validator("name", mode="wrap")
    @classmethod
    def set_name_wrap(cls, value, handler, info):
        print("field_validator->wrap")
        handler(value)
        return value

    @field_validator("name", mode="plain")
    @classmethod
    def set_name_plain(cls, value):
        print("field_validator->plain")
        print(value)
        return value

    @model_serializer(mode='wrap')
    def get_serializer_wrap(self, nxt, info):
        print("model_serializer-->wrap")
        print(nxt(self))
        return nxt(self)

    @model_serializer(mode="plain")
    def get_serializer_plain(self):
        print("model_serializer-->plain")
        print({"name": self.name})
        return {"name": self.name}
    @field_serializer("name", mode="wrap")
    @staticmethod
    def get_name_wrap(value, handler, info):
        print("field_serializer-->wrap")
        print(value)
        print(handler)
        print(info)
        serialized_value = handler(value)+"wwww"
        print(serialized_value)
        return serialized_value
    @field_serializer("name", mode="plain")
    def get_name_plain(self, value):
        print("field_serializer-->plain")
        new_name = value + "pppp"
        return new_name



user = User(name="张三", age=99)
print(user.model_dump())
