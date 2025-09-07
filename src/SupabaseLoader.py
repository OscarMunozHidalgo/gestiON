import os
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()


class SupabaseLoader:
    def load(table):
        url= os.environ.get("SUPABASE_URL")
        key = os.environ.get("SUPABASE_KEY")
        supabase = create_client(url, key)

        print("url:",url)
        print("key:",key)

        data = supabase.table(table).select("*").execute()
        return data