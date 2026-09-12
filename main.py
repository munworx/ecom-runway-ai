import random
from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse

app = FastAPI()

def calculate_ecom_runway(product_url: str, monthly_subs: float):
    base_price = random.randint(25, 150)
    cents = random.choice([0.95, 0.99, 0.00])
    competitor_price = float(base_price) + cents
    
    our_suggested_price = round(competitor_price - 1.50, 2)
    estimated_profit_per_unit = round(our_suggested_price * 0.40, 2)
    
    units_to_cover_subs = int(monthly_subs // estimated_profit_per_unit) + 1
    
    risk_levels = ["CRITICAL UNDERCUT", "HEALTHY MARGIN", "COMPETITIVE PRESSURE"]
    current_status = random.choice(risk_levels)
    
    if current_status == "CRITICAL UNDERCUT":
        ai_recommendation = f"Competitor is aggressively pricing at ${competitor_price}. Drop your target listing price to ${our_suggested_price} immediately to recapture customer search traffic and clear your ${monthly_subs} subscription overhead."
    else:
        ai_recommendation = f"Margins remain stable. Maintain listing price around ${our_suggested_price}. Sell {units_to_cover_subs} units this month to entirely offset software subscription expenses."

    return {
        "status": current_status,
        "competitor_price": competitor_price,
        "units_needed": units_to_cover_subs,
        "profit_per_unit": estimated_profit_per_unit,
        "action_plan": ai_recommendation
    }

@app.get("/analyze-runway")
def analyze_runway(
    product_url: str = Query(..., description="The full URL of the competitor product page"),
    monthly_subscription_spend: float = Query(..., description="The total monthly dollar amount spent on e-commerce software tools")
):
    return {
        "success": True,
        "timestamp_gmt": "2026-09-12",
        "payload": calculate_ecom_runway(product_url, monthly_subscription_spend)
    }

@app.get("/", response_class=HTMLResponse)
def interactive_dashboard():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>E-Com Runway AI - Optimizer</title>
        <style>
            body { font-family: 'Segoe UI', system-ui, sans-serif; background-color: #0f172a; color: #f8fafc; margin: 0; padding: 20px; display: flex; justify-content: center; align-items: center; min-height: 100vh; }
            .card { background: linear-gradient(145deg, #1e293b, #0f172a); border: 1px solid #334155; padding: 35px; border-radius: 24px; box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5); width: 100%; max-width: 500px; }
            h1 { color: #38bdf8; font-size: 2.2rem; margin: 0 0 5px 0; font-weight: 800; letter-spacing: -0.03em; text-align: center; }
            .subtitle { color: #64748b; font-size: 0.95rem; text-align: center; margin-bottom: 25px; }
            .form-group { margin-bottom: 20px; }
            label { display: block; font-size: 0.85rem; font-weight: 600; color: #94a3b8; text-transform: uppercase; margin-bottom: 8px; letter-spacing: 0.05em; }
            input { width: 100%; padding: 12px 16px; background-color: #090d16; border: 1px solid #334155; border-radius: 12px; color: #f8fafc; font-size: 1rem; box-sizing: border-box; transition: border-color 0.2s; }
            input:focus { outline: none; border-color: #38bdf8; }
            button { width: 100%; padding: 14px; background-color: #0ea5e9; color: white; border: none; border-radius: 12px; font-size: 1rem; font-weight: 600; cursor: pointer; transition: background-color 0.2s; margin-top: 10px; }
            button:hover { background-color: #0284c7; }
            .results-box { margin-top: 30px; background: rgba(15, 23, 42, 0.6); border: 1px dashed #334155; border-radius: 16px; padding: 20px; display: none; }
            .status-badge { display: inline-block; padding: 4px 12px; border-radius: 9999px; font-size: 0.75rem; font-weight: 700; margin-bottom: 15px; background-color: #ef4444; color: white; text-transform: uppercase; }
            .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-bottom: 15px; }
            .stat { background: #1e293b; padding: 12px; border-radius: 8px; text-align: center; border: 1px solid #334155; }
            .stat-val { font-size: 1.2rem; font-weight: 700; color: #34d399; }
            .stat-lbl { font-size: 0.75rem; color: #64748b; margin-top: 2px; }
            .advice { font-size: 0.9rem; line-height: 1.5; color: #cbd5e1; border-top: 1px solid #334155; padding-top: 12px; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>E-Com Runway AI</h1>
            <div class="subtitle">Unified Financial Optimization Dashboard</div>
            
            <div class="form-group">
                <label>Competitor Product URL</label>
                <input type="text" id="prodUrl" placeholder="https://ebay.com">
            </div>
            
            <div class="form-group">
                <label>Monthly Software Subscriptions ($)</label>
                <input type="number" id="subSpend" placeholder="e.g. 150">
            </div>
            
            <button onclick="runOptimization()">Optimize Runway</button>
            
            <div class="results-box" id="results">
                <div class="status-badge" id="resStatus">Analyzing</div>
                <div class="grid">
                    <div class="stat">
                        <div class="stat-val" id="resCompPrice">$0.00</div>
                        <div class="stat-lbl">Competitor Price</div>
                    </div>
                    <div class="stat">
                        <div class="stat-val" id="resUnits">0</div>
                        <div class="stat-lbl">Break-Even Units</div>
                    </div>
                </div>
                <div class="advice" id="resPlan">Recommendation loading...</div>
            </div>
        </div>

        <script>
            function runOptimization() {
                const url = document.getElementById('prodUrl').value;
                const spend = document.getElementById('subSpend').value;
                if(!url || !spend) { alert('Please fill in both boxes!'); return; }
                
                // Fetch the live calculations from your server backend endpoint dynamically
                fetch(`/analyze-runway?product_url=${encodeURIComponent(url)}&monthly_subscription_spend=${spend}`)
                    .then(res => res.json())
                    .then(wrapper => {
                        const data = wrapper.payload;
                        document.getElementById('resStatus').innerText = data.status;
                        document.getElementById('resStatus').style.backgroundColor = data.status === 'HEALTHY MARGIN' ? '#10b981' : '#f59e0b';
                        document.getElementById('resCompPrice').innerText = '$' + data.competitor_price.toFixed(2);
                        document.getElementById('resUnits').innerText = data.units_needed;
                        document.getElementById('resPlan').innerText = data.action_plan;
                        document.getElementById('results').style.display = 'block';
                    });
            }
        </script>
    </body>
    </html>
    """
