import json
import ast
import _ast

app_name = ''

with open('cookie.json') as jsonfile:
    app_name = json.load(jsonfile)['app_name']

models = {}
# parse models.py
with open('%s/models.py' % app_name) as models_file:
    m = ast.parse(models_file.read())
    for i in m.body:
        if type(i) == _ast.ClassDef:
            models[i.name] = {}
            for x in i.body:
                if type(x) == _ast.Assign:
                    models[i.name][x.targets[0].id] = x.value.func.attr


serializer_names = [model+'Serializer' for model in models]

with open('%s/serializer.py' % app_name, 'w') as ser_file:
    def ser_class(model):
        s = "class %sSerializer(serializers.HyperlinkedModelSerializer):\n" % model
        s += "    class Meta:\n"
        s += "        model = %s\n" % model
        s += " "*8 + "fields = (" + ', '.join(["'%s'" % x for x in models[model]]) + ')\n'
        ser_file.write('\n')
        ser_file.write(s)


    import1 = 'from rest_framework import serializers\n'
    import2 = 'from base.models import ' + ', '.join([model for model in models])
    ser_file.write(import1)
    ser_file.write(import2 + '\n')
    for model in models:
        ser_class(model)
