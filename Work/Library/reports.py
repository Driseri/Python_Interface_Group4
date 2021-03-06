# -*- coding: utf-8 -*-
"""
Бригада 4 БИВ205
Д. Ященко
"""
import matplotlib
import pandas as pd



def make_full_db(mpf,fpf,spf):
    full_db = pd.DataFrame(columns=["id","name","grade","id_fs","name_fs",
                                    "id_sh","shsh","value_shsh"],dtype=int)
    for idx,row in mpf.iterrows():
        fs_name = fpf[fpf['id_fs'] == row['id_fs']].iloc[0]['name_fs']
        sh_name = spf[spf['id_sh'] == row['id_sh']].iloc[0]['shsh']
        val_count = spf[spf['id_sh'] == row['id_sh']].iloc[0]['value_shsh']

        ns = pd.DataFrame([[int(row["id"]),row["name"],int(row["grade"]),int(row["id_fs"]),
                            fs_name,int(row["id_sh"]),sh_name,int(val_count)]],
                            columns=["id","name","grade","id_fs","name_fs",
                                     "id_sh","shsh","value_shsh"])
        full_db = full_db.append(ns,ignore_index=True)
    return (full_db)


def pivot_table(index_a, values_a, db):

    index_a = list(index_a)
    values_a = list(values_a)

    result = pd.pivot_table(db, index=index_a, values=values_a)

    result.to_csv(r'..\Output\pivot table.txt')
