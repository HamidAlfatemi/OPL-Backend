# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `#managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AdminLog(models.Model):
    id = models.BigIntegerField(primary_key=True)
    action_time = models.DateField(blank=True, null=True)
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.SmallIntegerField(blank=True, null=True)
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('ContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        ##managed = False
        db_table = 'admin_log'


class Author(models.Model):
    author_id = models.BigIntegerField(db_column='Author_id', primary_key=True)  # Field name made lowercase.
    role = models.IntegerField(db_column='Role', blank=True, null=True)  # Field name made lowercase.
    affiliation_id = models.BigIntegerField(db_column='Affiliation_id', blank=True, null=True)  # Field name made lowercase.
    authordesc = models.TextField(db_column='AuthorDesc', blank=True, null=True)  # Field name made lowercase.
    ref = models.ForeignKey('Reference', models.DO_NOTHING, db_column='Ref_id', blank=True, null=True)  # Field name made lowercase.
    person = models.ForeignKey('User', models.DO_NOTHING, db_column='Person_id')  # Field name made lowercase.
    organization = models.ForeignKey('Organization', models.DO_NOTHING, db_column='Organization_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        ##managed = False
        db_table = 'author'


class Concept(models.Model):
    conc_id = models.BigIntegerField(db_column='Conc_id', primary_key=True)  # Field name made lowercase.
    ctitle = models.TextField(db_column='CTitle', blank=True, null=True)  # Field name made lowercase.
    cdesc = models.TextField(db_column='CDesc', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        ##managed = False
        db_table = 'concept'


class Contactinfo(models.Model):
    ci_id = models.BigIntegerField(db_column='CI_id', primary_key=True)  # Field name made lowercase.
    conttype = models.IntegerField(db_column='ContType', blank=True, null=True)  # Field name made lowercase.
    contact = models.CharField(db_column='Contact', max_length=255, blank=True, null=True)  # Field name made lowercase.
    organization = models.ForeignKey('Organization', models.DO_NOTHING, db_column='Organization_id', blank=True, null=True)  # Field name made lowercase.
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    ref = models.ForeignKey('Reference', models.DO_NOTHING, db_column='Ref_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        ##managed = False
        db_table = 'contactinfo'


class ContentType(models.Model):
    id = models.BigIntegerField(primary_key=True)
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        ##managed = False
        db_table = 'content_type'


class Education(models.Model):
    edu_id = models.BigIntegerField(db_column='Edu_id', primary_key=True)  # Field name made lowercase.
    edudegree = models.IntegerField(db_column='EduDegree', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        ##managed = False
        db_table = 'education'


class Field(models.Model):
    field_id = models.BigIntegerField(db_column='Field_id', primary_key=True)  # Field name made lowercase.
    fieldtitle = models.CharField(db_column='FieldTitle', max_length=255, blank=True, null=True)  # Field name made lowercase.
    engagement = models.IntegerField(db_column='Engagement', blank=True, null=True)  # Field name made lowercase.
    fielddesc = models.TextField(db_column='FieldDesc', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        ##managed = False
        db_table = 'field'


class FieldEducation(models.Model):
    edu = models.OneToOneField(Education, models.DO_NOTHING, db_column='Edu_id', primary_key=True)  # Field name made lowercase. The composite primary key (Edu_id, Field_id) found, that is not supported. The first column is selected.
    field = models.ForeignKey(Field, models.DO_NOTHING, db_column='Field_id')  # Field name made lowercase.

    class Meta:
        ##managed = False
        db_table = 'field_education'
        unique_together = (('edu', 'field'),)


class GroupPermission(models.Model):
    id = models.BigIntegerField(primary_key=True)
    group = models.ForeignKey('Groupu', models.DO_NOTHING, blank=True, null=True)
    permission = models.ForeignKey('Permission', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        ##managed = False
        db_table = 'group_permission'


class Groupu(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        ##managed = False
        db_table = 'groupu'


class Journal(models.Model):
    journal_id = models.BigIntegerField(db_column='Journal_id', primary_key=True)  # Field name made lowercase.
    journalname = models.CharField(db_column='JournalName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    impactf = models.DecimalField(db_column='ImpactF', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        ##managed = False
        db_table = 'journal'


class Migrations(models.Model):
    id = models.BigIntegerField(primary_key=True)
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateField(blank=True, null=True)

    class Meta:
        ##managed = False
        db_table = 'migrations'


class OpOp(models.Model):
    opop_id = models.BigIntegerField(db_column='OPOP_id', primary_key=True)  # Field name made lowercase.
    op_id1 = models.ForeignKey('Openproblem', models.DO_NOTHING, db_column='OP_id1')  # Field name made lowercase.
    op_id2 = models.ForeignKey('Openproblem', models.DO_NOTHING, db_column='OP_id2', related_name='opop_op_id2_set')  # Field name made lowercase.
    rela = models.ForeignKey('Relation', models.DO_NOTHING, db_column='Rela_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        ##managed = False
        db_table = 'op_op'


class OpenConc(models.Model):
    conc = models.OneToOneField(Concept, models.DO_NOTHING, db_column='Conc_id', primary_key=True)  # Field name made lowercase. The composite primary key (Conc_id, OP_id) found, that is not supported. The first column is selected.
    op = models.ForeignKey('Openproblem', models.DO_NOTHING, db_column='OP_id')  # Field name made lowercase.

    class Meta:
        ##managed = False
        db_table = 'open_conc'
        unique_together = (('conc', 'op'),)


class Openproblem(models.Model):
    op_id = models.BigIntegerField(db_column='OP_id', primary_key=True)  # Field name made lowercase.
    optitle = models.TextField(db_column='OPTitle', blank=True, null=True)  # Field name made lowercase.
    opdesc = models.TextField(db_column='OPDesc', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        ##managed = False
        db_table = 'openproblem'


class OrgOrg(models.Model):
    oo_id = models.BigIntegerField(db_column='OO_id', primary_key=True)  # Field name made lowercase.
    org_id1 = models.ForeignKey('Organization', models.DO_NOTHING, db_column='Org_id1')  # Field name made lowercase.
    org_id2 = models.ForeignKey('Organization', models.DO_NOTHING, db_column='Org_id2', related_name='orgorg_org_id2_set')  # Field name made lowercase.
    orgrelation = models.TextField(db_column='OrgRelation', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        ##managed = False
        db_table = 'org_org'


class OrgRole(models.Model):
    or_id = models.BigIntegerField(db_column='OR_id', primary_key=True)  # Field name made lowercase.
    org = models.ForeignKey('Organization', models.DO_NOTHING, db_column='Org_id')  # Field name made lowercase.
    role = models.ForeignKey('Role', models.DO_NOTHING, db_column='Role_id')  # Field name made lowercase.
    orgroledesc = models.TextField(db_column='OrgRoleDesc', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        ##managed = False
        db_table = 'org_role'


class Organization(models.Model):
    organization_id = models.BigIntegerField(db_column='Organization_id', primary_key=True)  # Field name made lowercase.
    ot = models.ForeignKey('Orgtype', models.DO_NOTHING, db_column='OT_id', blank=True, null=True)  # Field name made lowercase.
    pdt_id = models.BigIntegerField(db_column='PDT_id', blank=True, null=True)  # Field name made lowercase.
    orgtitle = models.CharField(db_column='OrgTitle', max_length=200, blank=True, null=True)  # Field name made lowercase.
    parent_org_id = models.BigIntegerField(db_column='Parent_org_id', blank=True, null=True)  # Field name made lowercase.
    olrole = models.IntegerField(db_column='OLRole', blank=True, null=True)  # Field name made lowercase.
    orgdesc = models.TextField(db_column='OrgDesc', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        ##managed = False
        db_table = 'organization'


class OrganizationRejion(models.Model):
    rejion = models.OneToOneField('Rejion', models.DO_NOTHING, db_column='Rejion_id', primary_key=True)  # Field name made lowercase. The composite primary key (Rejion_id, Organization_id) found, that is not supported. The first column is selected.
    organization = models.ForeignKey(Organization, models.DO_NOTHING, db_column='Organization_id')  # Field name made lowercase.

    class Meta:
        ##managed = False
        db_table = 'organization_rejion'
        unique_together = (('rejion', 'organization'),)


class OrganizationUser(models.Model):
    user = models.OneToOneField('User', models.DO_NOTHING, primary_key=True)  # The composite primary key (user_id, Organization_id) found, that is not supported. The first column is selected.
    organization = models.ForeignKey(Organization, models.DO_NOTHING, db_column='Organization_id')  # Field name made lowercase.
    jobtitle = models.IntegerField(db_column='JobTitle', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'organization_user'
        unique_together = (('user', 'organization'),)


class Orgtype(models.Model):
    ot_id = models.BigIntegerField(db_column='OT_id', primary_key=True)  # Field name made lowercase.
    typetitle = models.CharField(db_column='TypeTitle', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'orgtype'


class Permission(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=150, blank=True, null=True)
    content_type_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'permission'


class Qconcept(models.Model):
    qc_id = models.BigIntegerField(db_column='QC_id', primary_key=True)  # Field name made lowercase.
    qctitle = models.CharField(db_column='QCTitle', max_length=30, blank=True, null=True)  # Field name made lowercase.
    qcdesc = models.TextField(db_column='QCDesc', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'qconcept'


class Question(models.Model):
    question_id = models.BigIntegerField(primary_key=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    excerpt = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    species = models.ForeignKey('QuestionsSpecies', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    question = models.IntegerField(db_column='Question', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'question'


class QuestionConcept(models.Model):
    qc = models.OneToOneField(Qconcept, models.DO_NOTHING, db_column='QC_id', primary_key=True)  # Field name made lowercase. The composite primary key (QC_id, question_id) found, that is not supported. The first column is selected.
    question = models.ForeignKey(Question, models.DO_NOTHING)

    class Meta:
        #managed = False
        db_table = 'question_concept'
        unique_together = (('qc', 'question'),)


class QuestionOp(models.Model):
    op = models.OneToOneField(Openproblem, models.DO_NOTHING, db_column='OP_id', primary_key=True)  # Field name made lowercase. The composite primary key (OP_id, question_id_id) found, that is not supported. The first column is selected.
    question_id = models.ForeignKey(Question, models.DO_NOTHING)

    class Meta:
        #managed = False
        db_table = 'question_op'
        unique_together = (('op', 'question_id'),)


class QuestionQuestion(models.Model):
    qq_id = models.BigIntegerField(db_column='QQ_id', primary_key=True)  # Field name made lowercase.
    question_id1 = models.ForeignKey(Question, models.DO_NOTHING, db_column='Question_id1')  # Field name made lowercase.
    question_id2 = models.ForeignKey(Question, models.DO_NOTHING, db_column='Question_id2', related_name='questionquestion_question_id2_set')  # Field name made lowercase.
    relationrate = models.DecimalField(db_column='RelationRate', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    qrel = models.ForeignKey('Questionrelation', models.DO_NOTHING, db_column='QRel_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'question_question'


class QuestionReference(models.Model):
    question = models.OneToOneField(Question, models.DO_NOTHING, db_column='Question_id', primary_key=True)  # Field name made lowercase. The composite primary key (Question_id, Ref_id) found, that is not supported. The first column is selected.
    ref = models.ForeignKey('Reference', models.DO_NOTHING, db_column='Ref_id')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'question_reference'
        unique_together = (('question', 'ref'),)


class Questionrelation(models.Model):
    qrel_id = models.BigIntegerField(db_column='QRel_id', primary_key=True)  # Field name made lowercase.
    qrtitle = models.CharField(db_column='QRTitle', max_length=30, blank=True, null=True)  # Field name made lowercase.
    qrdesc = models.TextField(db_column='QRDesc', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'questionrelation'


class QuestionsSpecies(models.Model):
    species_id = models.BigIntegerField(primary_key=True)
    species_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'questions_species'


class QuestionsSubmittedquestions(models.Model):
    question_ptr = models.OneToOneField(Question, models.DO_NOTHING, primary_key=True)

    class Meta:
        #managed = False
        db_table = 'questions_submittedquestions'


class Reference(models.Model):
    ref_id = models.BigIntegerField(db_column='Ref_id', primary_key=True)  # Field name made lowercase.
    reftitle = models.TextField(db_column='RefTitle', blank=True, null=True)  # Field name made lowercase.
    full_citation = models.CharField(max_length=200, blank=True, null=True)
    doi = models.CharField(db_column='DOI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    relevance = models.DecimalField(db_column='Relevance', max_digits=8, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    publishyear = models.DecimalField(db_column='PublishYear', max_digits=4, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    publishmonth = models.DecimalField(db_column='PublishMonth', max_digits=2, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    isbn = models.TextField(db_column='ISBN', blank=True, null=True)  # Field name made lowercase.
    journal = models.ForeignKey(Journal, models.DO_NOTHING, blank=True, null=True)
    rtype = models.ForeignKey('Reftype', models.DO_NOTHING, db_column='RType_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'reference'


class Reftype(models.Model):
    rtype_id = models.BigIntegerField(db_column='RType_id', primary_key=True)  # Field name made lowercase.
    ref_rtype = models.ForeignKey('self', models.DO_NOTHING, db_column='Ref_RType_id', blank=True, null=True)  # Field name made lowercase.
    rtype = models.CharField(db_column='RType', max_length=30, blank=True, null=True)  # Field name made lowercase.
    classdesc = models.TextField(db_column='ClassDesc', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'reftype'


class Rejion(models.Model):
    rejion_id = models.BigIntegerField(db_column='Rejion_id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'rejion'


class Relation(models.Model):
    rela_id = models.BigIntegerField(db_column='Rela_id', primary_key=True)  # Field name made lowercase.
    rtitle = models.TextField(db_column='RTitle', blank=True, null=True)  # Field name made lowercase.
    rdesc = models.TextField(db_column='RDesc', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'relation'


class Role(models.Model):
    role_id = models.BigIntegerField(db_column='Role_id', primary_key=True)  # Field name made lowercase.
    roletitle = models.CharField(db_column='RoleTitle', max_length=255, blank=True, null=True)  # Field name made lowercase.
    roledesc = models.TextField(db_column='RoleDesc', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'role'


class Session(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    session_date = models.DateField(blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'session'


class Theory(models.Model):
    theory_id = models.BigIntegerField(db_column='Theory_id', primary_key=True)  # Field name made lowercase.
    theorytitle = models.CharField(db_column='TheoryTitle', max_length=40, blank=True, null=True)  # Field name made lowercase.
    theorydesc = models.TextField(db_column='TheoryDesc', blank=True, null=True)  # Field name made lowercase.
    parent_t = models.ForeignKey('self', models.DO_NOTHING, db_column='Parent_T_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'theory'


class TheoryQuestion(models.Model):
    opinion = models.OneToOneField(Question, models.DO_NOTHING, db_column='Opinion_id', primary_key=True)  # Field name made lowercase. The composite primary key (Opinion_id, species_id, Theory_id) found, that is not supported. The first column is selected.
    species_id = models.BigIntegerField()
    theory = models.ForeignKey(Theory, models.DO_NOTHING, db_column='Theory_id')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'theory_question'
        unique_together = (('opinion', 'species_id', 'theory'),)


class TheoryReference(models.Model):
    ref = models.OneToOneField(Reference, models.DO_NOTHING, db_column='Ref_id', primary_key=True)  # Field name made lowercase. The composite primary key (Ref_id, Theory_id) found, that is not supported. The first column is selected.
    theory = models.ForeignKey(Theory, models.DO_NOTHING, db_column='Theory_id')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'theory_reference'
        unique_together = (('ref', 'theory'),)


class User(models.Model):
    id = models.BigIntegerField(primary_key=True)
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateField(blank=True, null=True)
    is_superuser = models.IntegerField(blank=True, null=True)
    username = models.CharField(max_length=150, blank=True, null=True)
    firstname = models.CharField(db_column='FirstName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    is_staff = models.IntegerField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    date_joined = models.DateField(blank=True, null=True)
    userdesc = models.TextField(db_column='UserDesc', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'user'


class UserEducation(models.Model):
    edu = models.OneToOneField(Education, models.DO_NOTHING, db_column='Edu_id', primary_key=True)  # Field name made lowercase. The composite primary key (Edu_id, User_id) found, that is not supported. The first column is selected.
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='User_id')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'user_education'
        unique_together = (('edu', 'user'),)


class UserField(models.Model):
    field = models.OneToOneField(Field, models.DO_NOTHING, db_column='Field_id', primary_key=True)  # Field name made lowercase. The composite primary key (Field_id, user_id) found, that is not supported. The first column is selected.
    user = models.ForeignKey(User, models.DO_NOTHING)

    class Meta:
        #managed = False
        db_table = 'user_field'
        unique_together = (('field', 'user'),)


class UserGroups(models.Model):
    id = models.BigIntegerField(primary_key=True)  # The composite primary key (id, group_id, user_id) found, that is not supported. The first column is selected.
    user = models.ForeignKey(User, models.DO_NOTHING)
    group = models.ForeignKey(Groupu, models.DO_NOTHING)

    class Meta:
        #managed = False
        db_table = 'user_groups'
        unique_together = (('id', 'group', 'user'),)


class UserPermission(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    permission = models.ForeignKey(Permission, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'user_permission'


class UserRejion(models.Model):
    rejion = models.OneToOneField(Rejion, models.DO_NOTHING, db_column='Rejion_id', primary_key=True)  # Field name made lowercase. The composite primary key (Rejion_id, user_id) found, that is not supported. The first column is selected.
    user = models.ForeignKey(User, models.DO_NOTHING)

    class Meta:
        #managed = False
        db_table = 'user_rejion'
        unique_together = (('rejion', 'user'),)


class UserRole(models.Model):
    ur_id = models.BigIntegerField(db_column='UR_id', primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey(User, models.DO_NOTHING)
    role = models.ForeignKey(Role, models.DO_NOTHING, db_column='Role_id')  # Field name made lowercase.
    roledesc = models.TextField(db_column='RoleDesc', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'user_role'
