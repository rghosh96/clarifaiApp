from app import app
from flask import render_template, request, redirect, url_for
from clarifai.rest import ClarifaiApp

def useClarify(image):
    # clarifai things	
    app = ClarifaiApp()
    def get_relevant_tags(image_url):
        response_data = app.tag_urls([image_url])

        tag_urls = []
        for concept in response_data['outputs'][0]['data']['concepts']:
            tag_urls.append(concept['name'])

        return tag_urls

    # print('\n'.join(get_relevant_tags(image)))
    return get_relevant_tags(image)
    

@app.route("/", methods=["GET", "POST"])
def upload():

    if request.method == "POST":
        req = request.form
        link = req.get("url")
        print(link)
        tags = useClarify(link)
        print('\n'.join(tags))


        return render_template("result.html", tags=tags, link=link)
	
    return render_template("index.html")

# @app.route("/results")
# def results():
	
#     return render_template("result.html")
