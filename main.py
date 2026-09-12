import random
from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse

app = FastAPI()

def calculate_ecom_runway(product_url: str, monthly_subs: float):
    base_price = random.randint(25, 150)
    cents = random.choice([0.95, 0.99, 0.00])
    competitor_price = float(base_price) + cents
    our_suggested_price = round(competitor_price - 1.50, 2)
    premium_target_price = round(competitor_price * 1.15, 2) # 15% brand markup simulation
    estimated_profit_per_unit = round(our_suggested_price * 0.40, 2)
    units_to_cover_subs = int(monthly_subs // estimated_profit_per_unit) + 1
    
    # Calculate a simulated progress performance metric
    efficiency_percentage = min(100, int((units_to_cover_subs * estimated_profit_per_unit / (monthly_subs + 1)) * 100))
    
    risk_levels = ["CRITICAL UNDERCUT", "HEALTHY MARGIN", "COMPETITIVE PRESSURE"]
    current_status = random.choice(risk_levels)
    
    if current_status == "CRITICAL UNDERCUT":
        ai_recommendation = f"⚠️ <strong>Risk Alert:</strong> Competitor is aggressively pricing at ${competitor_price}. Drop target price to <strong>${our_suggested_price}</strong> immediately to secure traffic and clear your ${monthly_subs} tools bleed."
    else:
        ai_recommendation = f"✅ <strong>System Healthy:</strong> Margins stable. Hold target velocity at <strong>${our_suggested_price}</strong>. Alternatively, scale premium branding value caps to <strong>${premium_target_price}</strong>."

    return {
        "status": current_status,
        "competitor_price": competitor_price,
        "premium_target": premium_target_price,
        "units_needed": units_to_cover_subs,
        "progress_rate": efficiency_percentage,
        "action_plan": ai_recommendation
    }

@app.get("/analyze-runway")
def analyze_runway(
    product_url: str = Query(..., description="The full URL of the competitor product page"),
    monthly_subscription_spend: float = Query(..., description="The total monthly dollar amount spent on tools")
):
    return {"success": True, "payload": calculate_ecom_runway(product_url, monthly_subscription_spend)}

@app.get("/", response_class=HTMLResponse)
def premium_dashboard():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>E-Com Runway AI Enterprise</title>
        <style>
            body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background-color: #0b0f19; color: #f8fafc; margin: 0; padding: 20px; display: flex; justify-content: center; align-items: center; min-height: 100vh; }
            .card { background: linear-gradient(160deg, #1e293b, #0f172a); border: 1px solid #334155; padding: 35px; border-radius: 28px; width: 100%; max-width: 520px; box-shadow: 0 30px 60px rgba(0,0,0,0.6); }
            .header-zone { text-align: center; margin-bottom: 25px; border-bottom: 1px dashed #334155; padding-bottom: 20px; }
            h1 { color: #38bdf8; font-size: 2.4rem; margin: 0 0 6px 0; font-weight: 800; letter-spacing: -0.04em; }
            .subtitle { color: #94a3b8; font-size: 0.95rem; }
            .form-group { margin-bottom: 18px; }
            label { display: block; font-size: 0.8rem; font-weight: 700; color: #cbd5e1; text-transform: uppercase; margin-bottom: 8px; letter-spacing: 0.05em; }
            input { width: 100%; padding: 14px 16px; background-color: #060911; border: 1px solid #475569; border-radius: 14px; color: #f8fafc; font-size: 1rem; box-sizing: border-box; }
            button { width: 100%; padding: 16px; background: linear-gradient(135deg, #0ea5e9, #2563eb); color: white; border: none; border-radius: 14px; font-size: 1.05rem; font-weight: 700; cursor: pointer; margin-top: 10px; box-shadow: 0 10px 20px rgba(14,165,233,0.2); }
            .results-box { margin-top: 30px; background: #060911; border: 1px solid #1e293b; border-radius: 20px; padding: 24px; display: none; }
            .status-line { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; }
            .status-badge { padding: 6px 16px; border-radius: 9999px; font-size: 0.75rem; font-weight: 800; text-transform: uppercase; color: white; }
            .grid-3 { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 12px; margin-bottom: 20px; }
            .stat { background: #1e293b; padding: 12px; border-radius: 12px; text-align: center; border: 1px solid #334155; }
            .stat-val { font-size: 1.25rem; font-weight: 800; color: #34d399; }
            .stat-lbl { font-size: 0.7srem; color: #94a3b8; text-transform: uppercase; margin-top: 4px; font-size: 0.65rem; }
            .progress-container { margin-bottom: 20px; background: rgba(30,41,59,0.3); padding: 12px; border-radius: 12px; border: 1px solid #1e293b; }
            .progress-bar { height: 8px; background-color: #1e293b; border-radius: 9999px; overflow: hidden; position: relative; margin-top: 6px; }
            .progress-fill { height: 100%; background: linear-gradient(90deg, #34d399, #38bdf8); width: 0%; transition: width 0.4s ease-out; }
            .advice { font-size: 0.95rem; line-height: 1.6; color: #e2e8f0; background: rgba(30,41,59,0.4); border-radius: 12px; padding: 14px; border-left: 4px solid #38bdf8; }
        </style>
    </head>
    <body>
        <div class="card">
            <div class="header-zone">
                <h1>⚡ E-Com Runway AI</h1>
                <div class="subtitle">Enterprise Level Financial Protection & Competitor Radar</div>
            </div>
            <div class="form-group">
                <label>🔗 Competitor Product Target URL</label>
                <input type="text" id="prodUrl" placeholder="https://amazon.com">
            </div>
            <div class="form-group">
                <label>💰 Monthly Tool Subscription Burn ($)</label>
                <input type="number" id="subSpend" placeholder="e.g. 150">
            </div>
            <button onclick="runOptimization()">🚀 Run Cloud Analytics</button>
            <div class="results-box" id="results">
                <div class="status-line">
                    <span style="font-size: 0.85rem; color:#64748b; font-weight:700; text-transform:uppercase;">Network Logs: <span style="color:#34d399">260ms</span></span>
                    <div class="status-badge" id="resStatus">Analyzing</div>
                </div>
                <div class="grid-3">
                    <div class="stat">
                        <div class="stat-val" id="resCompPrice">$0.00</div>
                        <div class="stat-lbl">Floor Price</div>
                    </div>
                    <div class="stat">
                        <div class="stat-val" id="resPremium">$0.00</div>
                        <div class="stat-lbl">Premium Target</div>
                    </div>
                    <div class="stat">
                        <div class="stat-val" id="resUnits">0</div>
                        <div class="stat-lbl">Target Sales</div>
                    </div>
                </div>
                <div class="progress-container">
                    <div style="display:flex; justify-content:space-between; font-size:0.75rem; color:#94a3b8; font-weight:600;">
                        <span>OVERHEAD CLEARANCE RADAR</span>
                        <span id="progressText">0%</span>
                    </div>
                    <div class="progress-bar"><div class="progress-fill" id="pFill"></div></div>
                </div>
                <div class="advice" id="resPlan">Loading...</div>
            </div>
        </div>
        <script>
            function runOptimization(){
                const url = document.getElementById("prodUrl").value;
                const spend = document.getElementById("subSpend").value;
                if(!url || !spend){ alert("Please fill out both entry fields!"); return; }
                fetch("/analyze-runway?product_url=" + encodeURIComponent(url) + "&monthly_subscription_spend=" + spend)
                    .then(res => res.json())
                    .then(wrapper => {
                        const data = wrapper.payload;
                        document.getElementById("resStatus").innerText = data.status;
                        document.getElementById("resStatus").style.backgroundColor = data.status === "HEALTHY MARGIN" ? "#059669" : "#d97706";
                        document.getElementById("resCompPrice").innerText = "$" + data.competitor_price.toFixed(2);
                        document.getElementById("resPremium").innerText = "$" + data.premium_target.toFixed(2);
                        document.getElementById("resUnits").innerText = data.units_needed + " Units";
                        
                        // Interactive graph processing adjustments
                        const percentage = data.progress_rate;
                        document.getElementById("pFill").style.width = percentage + "%";
                        document.getElementById("progressText").innerText = percentage + "% EFFICIENCY";
                        
                        document.getElementById("resPlan").innerHTML = data.action_plan;
                        document.getElementById("results").style.display = "block";
                    });
            }
        </script>
    </body>
    </html>
    """
    return html_content
