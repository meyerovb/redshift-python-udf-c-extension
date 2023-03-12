# redshift-python-udf-c-extension
Amazon doesn't document it, but redshift won't run python c extensions

Compiled [this](https://gist.github.com/Artanis/1223762) into the .so file using python 2.7.18 on an aws cloudshell.
Run "python ctest.py" and you'll see it works fine
Zip it up (don't zip the folder you put them in, just the files in the repo)
Put it into s3 and try this:

create or replace library testpackage language plpythonu from 's3://mybucket/testpy.zip'
    with credentials as 'aws_iam_role=ARN_OF_ROLE_REDSHIFT_USES'

CREATE OR REPLACE FUNCTION test(works bool)
RETURNS varchar IMMUTABLE AS $$
    from testpackage import testmodule
    return testmodule.testclass.works() if works else testmodule.testclass.broken()
$$ LANGUAGE plpythonu;

select test(true);

select test(false);

--select * from svl_udf_log order by created desc limit 1

Notice how the first test works, second test, not so much...
