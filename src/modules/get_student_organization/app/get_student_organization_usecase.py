from src.shared.domain.entities.student_organization import StudentOrganization
from src.shared.domain.repositories.student_organization_repository_interface import IStudentOrganizationRepository
from src.shared.helpers.errors.controller_errors import WrongTypeParameter, MissingParameters
from src.shared.helpers.errors.usecase_errors import NoItemsFound



class GetStudentOrganizationsUsecase:

    def __init__(self, repo: IStudentOrganizationRepository):
        self.repo = repo
    
    def __call__(self, stu_org_id: str):

        if not self.repo.get_stu_org(stu_org_id):
            raise NoItemsFound("Student Organization not found")
        
        return self.repo.get_stu_org(stu_org_id)
