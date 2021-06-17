import matplotlib
import pandas as pd



def make_full_db(mpf,fpf,spf):
    full_db = pd.DataFrame(columns=["id","name","grade","id_fs","name_fs",
                                    "id_sh","shsh","value_shsh"])
    for idx,row in mpf.iterrows():
        fs_name = fpf[fpf['id_fs'] == row['id_fs']].iloc[0]['name_fs']
        sh_name = spf[spf['id_sh'] == row['id_sh']].iloc[0]['shsh']
        val_count = spf[spf['id_sh'] == row['id_sh']].iloc[0]['value_shsh']

        ns = pd.DataFrame([[row["id"],row["name"],row["grade"],row["id_fs"],
                            fs_name,row["id_sh"],sh_name,val_count]],
                            columns=["id","name","grade","id_fs","name_fs",
                                     "id_sh","shsh","value_shsh"])
        full_db = full_db.append(ns,ignore_index=True)

    return (full_db)
