import functools
import inspect
import typing
from typing import Dict

from flask import request
from marshmallow import Schema

from common.configuration.config_source.ConfigContext import ConfigContext

context = ConfigContext()


def publish_message_after(payload: any, exchange: str, routing_key: str):
    def decorator_publish_message_after(func):
        @functools.wraps(func)
        def wrapper_publish_message_after(*args, **kwargs):
            channel = context.amqp_connection.channel()
            func(*args, **kwargs)
            channel.basic_publish(exchange=exchange, routing_key=routing_key, body=payload)
            return

        return wrapper_publish_message_after

    return decorator_publish_message_after


def serialize(result_schema, collection: bool = False):
    def decorator_serialize(func):
        @functools.wraps(func)
        def wrapper_serialize(*args, **kwargs):
            schema = result_schema(many=collection)
            return schema.dump(func(*args, **kwargs))

        return wrapper_serialize

    return decorator_serialize


def inject_request_body(body_schema: typing.Type[Schema]):
    """
    usege:
        @inject_request_body(TestSchema)
    :param body_schema:
    :return:
    """

    def decorator_inject(func):
        @functools.wraps(func)
        def wrapper_inject(*args, **kwargs):
            model = request.json

            schema = body_schema()
            result = schema.load(model)
            return func(result)

        return wrapper_inject

    return decorator_inject


def inject_query_params(default_values: Dict):
    """
    usage:
        @inject_query_params(default_values={
            'param1': {'default_value': [], 'type': list},
            'param2': {'default_value': 10, 'type': int},
        })
    :return:
    """

    def decorator_inject(func):
        param_names = default_values.keys() | inspect.getfullargspec(func).args

        @functools.wraps(func)
        def wrapper_inject(*args, **kwargs):
            injected_params = dict(kwargs)
            # this shit wack
            for parameter_name in param_names:
                if parameter_name in request.args:
                    injected_params[parameter_name] = \
                        request.args.get(parameter_name) \
                            if default_values[parameter_name]['type'] is None \
                            else default_values[parameter_name]['type'](request.args.get(parameter_name)) \
                            if default_values[parameter_name]['type'] != list \
                            else request.args.get(parameter_name).split(',')
                else:
                    if default_values.get(parameter_name) is not None:
                        injected_params[parameter_name] = default_values[parameter_name]['default_value']
                    else:
                        injected_params[parameter_name] = None
            return func(**injected_params)

        return wrapper_inject

    return decorator_inject
