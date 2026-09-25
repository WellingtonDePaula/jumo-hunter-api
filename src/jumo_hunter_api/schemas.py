from marshmallow import Schema, fields, validate

class StepSchema(Schema):
    observation = fields.List(fields.Float(),
                              required=True,
                              validate=validate.Length(equal=2)
                              )
    reward = fields.Float(required=True)
    done = fields.Boolean(required=True)