from api.utils.common import read_yaml
api_ = read_yaml('/home/rajan/GPT-Work/crediantials/crediatial.yml')

api_key = api_['OPENAI_API_SECRET']
print(api_key)