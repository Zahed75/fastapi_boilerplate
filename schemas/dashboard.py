from pydantic import BaseModel


class DashboardStatus(BaseModel):
    total_customer:int
    total_product:int
    total_categories:int
    total_invoices:int
    total_revenue:int


