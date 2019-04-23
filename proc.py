import pickle
import matplotlib.pyplot as plt
import argparse
parser = argparse.ArgumentParser(description='filter')
parser.add_argument('--school', type=str,default='',
                        help='school name')
parser.add_argument('--name',type=str, default="",
                        help='participant name')
parser.add_argument('--award',type=str,default='',
                        help='award type')
parser.add_argument('--control',type=int,default=-1,
                        help='control num')
parser.add_argument('--print-cert',action='store_true')
parser.add_argument('--file',type=str,default='anony.s')
args = parser.parse_args()

def sort_zip(keys,ct):
    return sorted(zip(keys,ct),key=lambda t:t[1],reverse=True)

def calibrate_sc(sc):
    sc=sc.replace('beiying','beijing')
    sc=sc.replace('\n',' ')
    sc=sc.replace('j i','ji')
    sc=sc.replace('beiing','beijing')
    sc=sc.replace('being','beijing')
    sc=sc.replace('!','i')
    sc=sc.replace('scnool','school')
    sc=sc.replace('1','i')
    sc=sc.replace('\'',' ')
    return sc


fs=[args.file]
name_spec=args.name
school_spec=args.school
award_spec=args.award
control_spec=-1 if args.control==-1 else args.control-1000000
print_cert=args.print_cert
awards={}
schools={}
total_count=0
Hono={}
Meri={}
Outs={}
Final={}
Best={}
for f_name in fs:
    f=open(f_name,'rb')
    certs=pickle.load(f)
    for i,cert in enumerate(certs):     
        sc=cert.school.lower()
        sc=calibrate_sc(sc)
        if not award_spec in cert.award.lower():
            continue
        if not school_spec in sc:
            continue
        if sum([name_spec in nme.lower() for nme in cert.names])==0:
            continue
        if not control_spec==-1:
            if not control_spec==cert.no:
                continue
        if print_cert:
            print(cert.names,'\n',cert.award,'\n',cert.school,'\n')
        total_count+=1
        if schools.get(sc)==None:
            schools[sc]=1
        else:
            schools[sc]+=1
        names=[name.lower() for name in cert.names]
        if awards.get(cert.award)==None:
            awards[cert.award]=1
        else:
            awards[cert.award]+=1
        aw=cert.award.lower()
        if 'honor' in aw:
            if Hono.get(sc)==None:
                Hono[sc]=1
            else:
                Hono[sc]+=1
        if 'meri' in aw:
            if Meri.get(sc)==None:
                Meri[sc]=1
            else:
                Meri[sc]+=1
        if 'outstanding' in aw:
            if Outs.get(sc)==None:
                Outs[sc]=1
            else:
                Outs[sc]+=1
            if Best.get(sc)==None:
                Best[sc]=1
            else:
                Best[sc]+=1
        if 'final' in aw:
            if Final.get(sc)==None:
                Final[sc]=1
            else:
                Final[sc]+=1
            if Best.get(sc)==None:
                Best[sc]=1
            else:
                Best[sc]+=1
        
print('\n')
award_types=[]
award_count=[]
for key in awards:
    award_types.append(key)
    award_count.append(awards[key])

school_names=[]
school_count=[]

for school in schools:
    school_names.append(school)
    school_count.append(schools[school])

school_list=sort_zip(school_names,school_count)
award_list=sort_zip(award_types,award_count)

for a,c in award_list:
    print(a,'\t',c,"\t",round(c/total_count*100,2),'%')


for s,c in school_list:
    print(c,'\t',s)
print('total',total_count)
'''
perc_school=[]
perc=[]
cts=[]
for key in Best:
    n=Best[key]
    tot=schools[key]
    per=n/tot
    perc_school.append(key)
    perc.append(per)
    cts.append(tot)
a=sort_list(perc_school,perc)

print("O\tF\tM\tH\tTeam num")
for s,c in school_list:
    tot=schools[s]
    fi=0 if Final.get(s)==None else Final[s]
    #fi=round(fi*100/tot,2)
    ou=0 if Outs.get(s)==None else Outs[s]
    #ou=round(ou*100/tot,2)
    me=0 if Meri.get(s)==None else Meri[s]
    #me=round(me*100/tot,2)
    ho=0 if Hono.get(s)==None else Hono[s]
    #ho=round(ho*100/tot,2)
    
    print("{}\t{}\t{}\t{}\t{}\t{}".format(ou,fi,me,ho,tot,s))
'''
