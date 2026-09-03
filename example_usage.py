from client import MerchantDynamicPricingElasticityOptimizerClient

def main():
    client = MerchantDynamicPricingElasticityOptimizerClient()
    res = client.optimize_price_elasticity('SKU-101', 199.00, 90.00, 189.00)
    print('Merchant Dynamic Pricing Optimizer: ' + res['pricing_optimization_id'] + ' (SKU: ' + res['sku_id'] + ')')
    print('Adjusted Price: $' + str(res['recommended_adjusted_price_usd']) + ' (Margin: ' + str(res['projected_gross_margin_pct']) + '%)')
    print('Sales Lift: +' + str(res['projected_unit_sales_lift_pct']) + '% | Profit Lift: +' + str(res['projected_total_profit_lift_pct']) + '%')
    print('Simulation URL: ' + res['elasticity_simulation_chart_url'])

if __name__ == '__main__':
    main()
