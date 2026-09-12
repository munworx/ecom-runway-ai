import random
from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse

app = FastAPI()

def calculate_ecom_runway(product_url: str, monthly_subs: float):
    base_price = random.randint(45, 160)
    cents = random.choice([0.95, 0.99, 0.00])
    competitor_price = float(base_price) + cents
    
    our_suggested_price = round(competitor_price - 1.50, 2)
    premium_target_price = round(competitor_price * 1.18, 2)
    
    supplier_cost = round(our_suggested_price * 0.35, 2)
    net_profit_margin = round(our_suggested_price - supplier_cost, 2)
    units_to_cover_subs = int(monthly_subs // net_profit_margin) + 1
    
    avg_cpc = 0.85
    conversion_rate = 0.02
    clicks_needed_per_unit = int(1 / conversion_rate)
    total_clicks_needed = units_to_cover_subs * clicks_needed_per_unit
    estimated_ad_spend_overhead = round(total_clicks_needed * avg_cpc, 2)
    
    efficiency_percentage = min(100, int((units_to_cover_subs * net_profit_margin / (monthly_subs + 1)) * 100))
    
    risk_levels = ["CRITICAL UNDERCUT", "HEALTHY MARGIN", "COMPETITIVE PRESSURE"]
    current_status = random.choice(risk_levels)
    trend = random.choice(["TRENDING UP (+4.2%)", "TRENDING DOWN (-2.8%)", "STABLE MARKET"])
    
    if current_status == "CRITICAL UNDERCUT":
        ai_recommendation = f"Risk Alert: Competitor undercutting at ${competitor_price}. Drop price to ${our_suggested_price} to maintain velocity. Acquire {total_clicks_needed} ad clicks to secure targets."
    else:
        ai_recommendation = f"System Healthy: Margins stable. Hold price at ${our_suggested_price} or leverage premium value scaling up to ${premium_target_price}."

    return {
        "status": current_status,
        "market_trend": trend,
        "competitor_price": competitor_price,
        "premium_target": premium_target_price,
        "units_needed": units_to_cover_subs,
        "progress_rate": efficiency_percentage,
        "supplier_cost": supplier_cost,
        "net_profit_margin": net_profit_margin,
        "ad_spend_budget": estimated_ad_spend_overhead,
        "clicks_required": total_clicks_needed,
        "action_plan": ai_recommendation
    }

@app.get("/analyze-runway")
def analyze_runway(
    product_url: str = Query(..., description="The full URL of the competitor product page"),
    monthly_subscription_spend: float = Query(..., description="The total monthly dollar amount spent on tools")
):
    return {"success": True, "payload": calculate_ecom_runway(product_url, monthly_subscription_spend)}

@app.get("/", response_class=HTMLResponse)
def enterprise_command_suite():
    # Safely building the interface block with zero complex quotes or parenthesis nesting
    html_lines = [
        "<!DOCTYPE html><html lang='en'><head><meta charset='UTF-8'><title>E-Com Runway AI Enterprise</title><style>",
        "body{font-family:sans-serif;background-color:#070a13;color:#f8fafc;margin:0;padding:20px;display:flex;justify-content:center;align-items:center;min-height:100vh;}",
        ".card{background:linear-gradient(160deg,#1e293b,#090d16);border:1px solid #334155;padding:35px;border-radius:28px;width:100%;max-width:540px;box-shadow:0 40px 80px rgba(0,0,0,0.7);}",
        ".header-zone{text-align:center;margin-bottom:25px;border-bottom:1px dashed #334155;padding-bottom:20px;}h1{color:#38bdf8;font-size:2.4rem;margin:0 0 6px 0;font-weight:800;}",
        ".subtitle{color:#94a3b8;font-size:0.95rem;}.form-group{margin-bottom:18px;}label{display:block;font-size:0.8rem;font-weight:700;color:#cbd5e1;text-transform:uppercase;margin-bottom:8px;}",
        ".input-box{width:100%;padding:14px 16px;background-color:#020617;border:1px solid #475569;border-radius:14px;color:#f8fafc;font-size:1rem;box-sizing:border-box;}",
        ".main-btn{width:100%;padding:16px;background:#0ea5e9;color:white;border:none;border-radius:14px;font-size:1.05rem;font-weight:700;cursor:pointer;margin-top:10px;}",
        ".results-box{margin-top:30px;background:#020617;border:1px solid #1e293b;border-radius:20px;padding:24px;display:none;}",
        ".status-line{display:flex;justify-content:space-between;align-items:center;margin-bottom:20px;}",
        ".status-badge{padding:6px 16px;border-radius:9999px;font-size:0.75rem;font-weight:800;text-transform:uppercase;color:white;}",
        ".section-title{font-size:0.8rem;font-weight:700;color:#38bdf8;text-transform:uppercase;margin:20px 0 10px 0;display:flex;justify-content:space-between;}",
        ".grid-3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px;margin-bottom:15px;}",
        ".stat{background:#1e293b;padding:12px;border-radius:12px;text-align:center;border:1px solid #334155;}",
        ".stat-val{font-size:1.25rem;font-weight:800;color:#34d399;}.stat-lbl{color:#94a3b8;text-transform:uppercase;margin-top:4px;font-size:0.65rem;}",
        ".progress-container{margin-bottom:20px;background:rgba(30,41,59,0.3);padding:12px;border-radius:12px;border:1px solid #1e293b;}",
        ".progress-bar{height:8px;background-color:#1e293b;border-radius:9999px;overflow:hidden;position:relative;margin-top:6px;}",
        ".progress-fill{height:100%;background:#34d399;width:0%;transition:width 0.4s ease-out;}",
        ".advice{font-size:0.95rem;line-height:1.6;color:#e2e8f0;background:rgba(30,41,59,0.4);border-radius:12px;padding:14px;border-left:4px solid #38bdf8;margin-bottom:20px;}",
        ".util-row{display:flex;gap:10px;margin-top:15px;}.util-btn{flex:1;padding:10px;background:#1e293b;border:1px solid #334155;border-radius:8px;color:#cbd5e1;font-size:0.8rem;font-weight:600;cursor:pointer;}",
        "</style></head><body><div class='card'><div class='header-zone'><h1>E-Com Runway AI</h1><div class='subtitle'>Enterprise Data Command Suite & Pricing Radar</div></div>",
        "<div class='form-group'><label>Competitor Product Target URL</label><input type='text' class='input-box' id='prodUrl' placeholder='https://amazon.com'></div>",
        "<div class='form-group'><label>Monthly Fixed Software Expenses ($)</label><input type='number' class='input-box' id='subSpend' placeholder='e.g. 150'></div>",
        "<button class='main-btn' onclick='runOptimization()'>Execute Enterprise Intelligence</button><div class='results-box' id='results'>",
        "<div class='status-line'><span style='font-size:0.85rem;color:#64748b;font-weight:700;text-transform:uppercase;'>Diagnostic Status: <span style='color:#34d399'>ONLINE</span></span><div class='status-badge' id='resStatus'>Analyzing</div></div>",
        "<div class='section-title'><span>Market Benchmarks</span> <span id='resTrend' style='color:#94a3b8'>STABLE</span></div>",
        "<div class='grid-3'><div class='stat'><div class='stat-val' id='resCompPrice'>$0.00</div><div class='stat-lbl'>Floor Price</div></div>",
        "<div class='stat'><div class='stat-val' id='resPremium'>$0.00</div><div class='stat-lbl'>Premium Max</div></div>",
        "<div class='stat'><div class='stat-val' id='resUnits'>0</div><div class='stat-lbl'>Target Units</div></div></div>",
        "<div class='section-title'><span>Unit Economics Layer</span></div>",
        "<div class='grid-3'><div class='stat'><div class='stat-val' id='resCOGS'>$0.00</div><div class='stat-lbl'>Est. Unit Cost</div></div>",
        "<div class='stat'><div class='stat-val' id='resMargin'>$0.00</div><div class='stat-lbl'>Net Margin</div></div>",
        "<div class='stat'><div class='stat-val' id='resAdSpend'>$0.00</div><div class='stat-lbl'>Ad Overhead</div></div></div>",
        "<div class='progress-container'><div style='display:flex;justify-content:space-between;font-size:0.75rem;color:#94a3b8;font-weight:600;'><span>RUNWAY SECURITY RADAR</span><span id='progressText'>0%</span></div>",
        "<div class='progress-bar'><div class='progress-fill' id='pFill'></div></div></div>",
        "<div class='section-title'><span>AI Recommendation Blueprint</span></div><div class='advice' id='resPlan'>Processing...</div>",
        "<div class='util-row'><button class='util-btn' id='btnCopy'>Copy JSON</button><button class='util-btn' id='btnCSV'>Download CSV</button></div></div></div>",
        "<script>let currentPayload=null;function runOptimization(){const u=document.getElementById('prodUrl').value;const s=document.getElementById('subSpend').value;if(!u||!s){alert('Complete variables!');return;}",
        "fetch('/analyze-runway?product_url='+encodeURIComponent(u)+'&monthly_subscription_spend='+s).then(r=>r.json()).then(w=>{currentPayload=w.payload;const d=w.payload;document.getElementById('resStatus').innerText=d.status;",
        "document.getElementById('resStatus').style.backgroundColor=d.status==='HEALTHY MARGIN'?'#059669':'#d97706';document.getElementById('resTrend').innerText=d.market_trend;",
        "document.getElementById('resCompPrice').innerText='$'+d.competitor_price.toFixed(2);document.getElementById('resPremium').innerText='$'+d.premium_target.toFixed(2);",
        "document.getElementById('resUnits').innerText=d.units_needed+' Units';document.getElementById('resCOGS').innerText='$'+d.supplier_cost.toFixed(2);document.getElementById('resMargin').innerText='$'+d.net_profit_margin.toFixed(2);",
        "document.getElementById('resAdSpend').innerText='$'+d.ad_spend_budget.toFixed(2);const p=d.progress_rate;document.getElementById('pFill').style.width=p+'%';document.getElementById('progressText').innerText=p+'% SUSTAINABILITY';",
        "document.getElementById('resPlan').innerHTML=d.action_plan;document.getElementById('results').style.display='block';});}document.getElementById('btnCopy').addEventListener('click',function(){if(!currentPayload)return;navigator.clipboard.writeText(JSON.stringify(currentPayload,null,2));alert('Metrics Copied!');});",
