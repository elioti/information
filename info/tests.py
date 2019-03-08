from django.test import TestCase

# Create your tests here.
# dict1 = [{"account":"31234124","name":"eqwe21","phone":"3123","qq":"3123","email":"2313","wechat":"23132d3e"},{"account":"02342","name":"31313","phone":"e1e12e1e","qq":"12","email":"dwqdq","wechat":"dede"},{"account":"4234","name":"313131","qq":"312313","email":"312312","wechat":"dede"},{"account":"4234","name":"131231","phone":"131321","qq":"31313","email":"132313","wechat":"31313"},{"account":"ddde1","name":"131312","phone":"14","email":"1","wechat":"dcd"},{"account":"123123","name":"dwdw1","phone":"e1e12e1e","qq":"5r","email":"343","wechat":"12313"},{"account":"das221","name":"312313","phone":"er234","qq":"3131","email":"1","wechat":"1.00E+12"}]
# validated_data = [
#             dict(list(attrs.items()) + list(kwargs.items()))
#             for attrs in dict1
#         ]
dict1 = {"account":"31234124","name":"eqwe21","phone":"3123","qq":"3123","email":"2313","wechat":"23132d3e"}

print(list(dict1.items()))