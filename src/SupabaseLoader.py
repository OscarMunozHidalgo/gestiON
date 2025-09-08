import os
from supabase import create_client

class SupabaseLoader:
    def load(url, key):
        supabase = create_client(url, key)
        return supabase