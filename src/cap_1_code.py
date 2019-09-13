import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.style.use("ggplot")

def read_data():
    mda_df = pd.read_csv('data/all_indicators_mda.csv')
    rom_df = pd.read_csv('data/all_indicators_rou.csv')
    ukr_df = pd.read_csv('data/all_indicators_ukr.csv')
    blr_df = pd.read_csv('data/all_indicators_blr.csv')
    geo_df = pd.read_csv('data/all_indicators_geo.csv')
    rus_df = pd.read_csv('data/all_indicators_rus.csv')
    fra_df = pd.read_csv('data/all_indicators_fra.csv')
    ger_df = pd.read_csv('data/all_indicators_deu.csv')
    gbr_df = pd.read_csv('data/all_indicators_gbr.csv')
    return mda_df, rom_df, ukr_df, blr_df, geo_df, rus_df, fra_df, ger_df, gbr_df

def transform_data():
    pivoted_mda = apply_methods(mda_df)
    pivoted_rom = apply_methods(rom_df)
    pivoted_ukr = apply_methods(ukr_df)
    pivoted_blr = apply_methods(blr_df)
    pivoted_geo = apply_methods(geo_df)
    pivoted_rus = apply_methods(rus_df)
    pivoted_fra = apply_methods(fra_df)
    pivoted_ger = apply_methods(ger_df)
    pivoted_gbr = apply_methods(gbr_df)
    return pivoted_mda, pivoted_rom, pivoted_ukr, pivoted_blr, pivoted_geo, pivoted_rus, pivoted_fra, pivoted_ger, pivoted_gbr

def reset_idx(df):
    return df.reset_index(inplace=True)

def drop_row(dataframe, row):
    return dataframe.drop([row], inplace=True)

def drop_columns(dataframe,column_list):
    return dataframe.drop(columns=column_list, inplace=True)

def column_to_numeric(dataframe,column_list):
    dataframe[column_list] = dataframe[column_list].apply(pd.to_numeric)

def drop_na(dataframe,column_name):
    return dataframe.dropna(subset=[column_name], inplace=True)

def pivot_dataframe(df, index, columns, values):
    df = df.pivot(index=index,columns=columns,values=values)
    df.sort_index(ascending=False,inplace=True)
    return df
    
def apply_methods(df):
    drop_row(df,0)
    column_to_numeric(df,cols_to_nums)
    drop_na(df, na_to_drop)
    df = pivot_dataframe(df, 'Year', 'Indicator Name', 'Value')
    reset_idx(df)
    return df

def plot_vert_line(ax, value,linestyle, color):
    ax.axvline(x=value, linestyle=linestyle, color=color)

def plot_line(ax, df, x_col, y_col, y_label, title, linewidth, alpha, color, legend=False, xlim=(1995,2017), ylim=False):
    year_list = list(range(xlim[0], xlim[1] + 1))
    x = df[x_col]
    y = df[y_col]
    ax.plot(x,y,linewidth=linewidth,alpha=alpha,color=color)
    ax.set_title(title, fontsize='xx-large', fontweight='bold' )
    ax.set_xlim(xlim)
    ax.set_xticks(year_list)
    ax.set_xticklabels(year_list,rotation=60, fontsize='xx-large', fontweight='bold')
    ax.set_ylabel(y_label, fontsize='xx-large', fontweight='heavy')
    ax.tick_params(axis="y", labelsize=20)
    if legend:
        ax.legend(legend,fontsize='xx-large')
    if ylim:
        ax.set_ylim(ylim)    

def plot_bar(ax, df, x_col, y_col, y_lable, x_font, y_font, title, title_font, color):
    x = df[x_col]
    y = df[y_col]
    ax.tick_params(axis="y", labelsize=20)
    ax.tick_params(axis='x', labelsize=x_font, labelrotation=50.0,)
    ax.set_ylabel(y_lable, fontsize=y_font, fontweight='bold')
    ax.bar(x,y,color=color)
    ax.set_title(title, fontsize=title_font)

   

if __name__ == '__main__':
    mda_df, rom_df, ukr_df, blr_df, geo_df, rus_df , fra_df, ger_df, gbr_df = read_data()
    cols_to_drop = ['Country ISO3', 'Country Name']
    cols_to_nums = ['Year', 'Value']
    na_to_drop = 'Value'
    pivoted_mda, pivoted_rom, pivoted_ukr, pivoted_blr, pivoted_geo, pivoted_rus, pivoted_fra, pivoted_ger, pivoted_gbr = transform_data()
    df_list = [pivoted_mda,pivoted_rom,pivoted_ukr,pivoted_blr, pivoted_geo,pivoted_rus,pivoted_fra,pivoted_ger, pivoted_gbr,]
    title_list_rec_sanc = ['Great Recession', 'Sanctions on Russia', 'Moldova', 'Romania','Ukraine',
                               'Belarus', 'Georgia', 'Russia', 'France', 'Germany', 'Great Britain']
    title_list_fall_rec_sanc = ['Fall of USSR', 'Great Recession', 'Sanctions on Russia', 'Moldova', 'Romania','Ukraine',
                               'Belarus', 'Georgia', 'Russia', 'France', 'Germany', 'Great Britain']
    title_list = ['Moldova', 'Romania','Ukraine','Belarus', 'Georgia', 'Russia', 'France', 'Germany', 'Great Britain', ]
    neighbor_df_list = [pivoted_mda,pivoted_rom,pivoted_ukr,pivoted_blr, pivoted_geo,pivoted_rus]
    neighbor_df_list_minus_bel_geo = [pivoted_mda, pivoted_rom, pivoted_ukr, pivoted_rus]
    neighbor_title_list_minus_bel_geo = ['Moldova', 'Romania','Ukraine','Russia']
    color_list_minus_bel_geo = ['yellow', 'darkgreen', 'aqua', 'red']
    neighbor_title_list_minus_bel_geo_rec_sanc = ['Great Recession', 'Sanctions on Russia', 'Moldova', 'Romania','Ukraine','Russia']
    neighbor_df_list_poverty = [pivoted_mda, pivoted_geo, pivoted_rus]
    color_list_poverty = ['yellow', 'dimgray', 'red']
    title_list_poverty = ['Russian Financial Crisis', 'Recovery due to Oil Price Increase', 'Moldova', 'Georgia', 'Russia']
    neighbor_title_poverty = ['Russian Financial Crisis', 'Moldova', 'Russia', 'Ukraine']
    neighbor_title_list_rec_sanc = ['Great Recession','Sanctions on Russia', 'Moldova', 'Romania','Ukraine','Belarus', 'Georgia', 'Russia', ]
    neighbor_title_list_fall_cris_recov = ['Fall of USSR', 'Russian Financial Crisis', 'Recovery due to Oil Price Increase', 'Moldova', 'Romania','Ukraine','Belarus', 'Georgia', 'Russia']
    neighbor_title_list = ['Moldova', 'Romania','Ukraine','Belarus', 'Georgia', 'Russia']
    color_list=['yellow','darkgreen','aqua', 'maroon', 'dimgray', 'red', 'lightsteelblue', 'darkorange', 'crimson']

