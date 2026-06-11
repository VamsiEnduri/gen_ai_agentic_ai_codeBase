SUPABASE_URL="https://jyhlamprzverrcrcwzdq.supabase.co"
SUPABASE_KEY="sb_publishable_8tF07bb4cciNIYUZpa4BuA_nyg-Jsak"

# pip install supabase
from supabase import create_client

supabase_c=create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)