
from flask_restful import Resource,  reqparse
from flask_jwt import  jwt_required
from models.store import StoreModel

class Store(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('store_id',
                            type=int,
                            required=True,
                            help="This should be provided!")                           

    @jwt_required()
    def get(self , name):
        store= StoreModel.find_by_name(name)
        if store:
            return store.json()
        else:
            return {"message":"No record Found"} , 404
    
    @jwt_required()
    def post(self , name):
        result = StoreModel.find_by_name(name)
        if result:
            return {'message':'An item with name {} already exist.'.format(name)} , 400

        data = Store.parser.parse_args()
        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {"message":"An exception has occured"},500
        return store.json(), 201


    def put(self, name):
        data = Store.parser.parse_args()
        store = StoreModel.find_by_name(name)
        if store is None:
            store = StoreModel(name)
        else:
            store.price = data['price']
        store.save_to_db()
        return store.json()


    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
        return {"message":"Deleted Succefully"}
        


    
class StoreList(Resource):
    def get(self):
        return {"items":[store.json() for store in StoreModel.query.all()]}