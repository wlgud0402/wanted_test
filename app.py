from flask_restx import Api
from search.views import Search_API
from tag.models import Tag, TagCountry
from tag.views import Tag_API
from company.views import Company_API
from company.models import Company, CompanyCountry
from server.config import app, db, ma

api = Api(
    app,
    version='0.1',
    title="김지형-원티드랩 API명세서",
    description="API경로, 파라미터, query등을 확인할 수 있는 API명세서 입니다.",
    terms_url="/",
    contact="jihyung.kim.dev@gmail.com",
    license="kim_jihyung"
)

api.add_namespace(Tag_API, '/api/tag')
api.add_namespace(Company_API, '/api/company')
api.add_namespace(Search_API, '/api/search')

# db.init_app(app)
# db.app = app
# db.create_all()

# Run Server
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000)
