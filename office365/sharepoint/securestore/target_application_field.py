from office365.runtime.paths.service_operation import ServiceOperationPath
from office365.runtime.queries.service_operation import ServiceOperationQuery
from office365.sharepoint.entity import Entity


class TargetApplicationField(Entity):
    """A name of a credential field and its associated credential type."""

    def __init__(self, context, name=None, masked=None, credential_type=None):
        params = {"name": name, "masked": masked, "credentialType": credential_type}
        static_path = ServiceOperationPath(
            "Microsoft.Office.SecureStoreService.Server.TargetApplicationField", params
        )
        super(TargetApplicationField, self).__init__(context, static_path)

    @staticmethod
    def create(context, name, masked, credential_type):
        """
        Creates a credential field

        :type context: office365.sharepoint.client_context.ClientContext
        :param str name:
        :param bool masked:
        :param int credential_type:
        """
        return_type = TargetApplicationField(context)
        payload = {"name": name, "masked": masked, "credentialType": credential_type}
        qry = ServiceOperationQuery(
            return_type, "", None, payload, None, return_type, True
        )
        context.add_query(qry)
        return return_type

    @property
    def entity_type_name(self):
        return "Microsoft.Office.SecureStoreService.Server.TargetApplicationField"
