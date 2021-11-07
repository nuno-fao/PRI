def get_true_discount(df):
    x = 0
    for _, row in df.iterrows():
        try:
            disc = row.get('discount_price')
            orig = row.get('original_price')
            disc = str(disc)
            if disc < orig:
                x+=1
        except:
            continue
    return x