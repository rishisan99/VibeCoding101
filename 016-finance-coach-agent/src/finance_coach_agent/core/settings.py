from pydantic import BaseModel


class AppInfo(BaseModel):
    api_title: str = "Finance Coach Agent"
    csv_fields: list[str] = ["date", "category", "amount", "note"]


app_info = AppInfo()
