from import_export import resources
from .models import Comp

class CompResource(resources.ModelResource):
    def before_import(self, dataset, using_transactions, dry_run, **kwargs):
        dataset.insert_col(0, col=["",]*dataset.height, header="id")

    def get_instance(self, instance_loader, row):
        return False

    class Meta:
        model = Comp
        skip_unchanged = True
        report_skipped = True
        export_order = ('name','date_ins','number','place','user','note','conf','os','msoffice','buh','mobile','inwork','decommissioned','bios1','biossuper')
