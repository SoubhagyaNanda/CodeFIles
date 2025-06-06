from flask import Flask, request, jsonify
app= Flask(__name__)  # --> Private variable


post= [
    {'id': 1, 'title': 'Hello', 'body': 'World'},
    {'id': 2, 'title': 'Test', 'body': 'Framework'}
]

@app.route('/posts',methods=['GET'])
def get_posts():
    return jsonify(post),200

@app.route('/posts/<int:post_id>',methods=['GET'])
def get_single_data(post_id):
    posts = next((i for i in post if i['id']==post_id),None)
    return jsonify(posts) if posts else ('Not found',404)


app.route('/post', methods=['POST'])
def apiCall():
    data= request.json
    newID= max(i['id'] for i in post)+1 if post else 1
    newPost= {'id': newID, 'title': data['title'], 'body': data['body']}
    post.append(newPost)
    return jsonify(newPost), 201

if __name__=='__main__':
    app.run(debug=True)