# Connector and implementation boundary

Read plans and supplied evidence before invoking a connector. Discover the actual authorised tool and inspect the current target before a change. A plan-only request authorises no infrastructure mutation.

Before any write, identify the account/project/environment, exact change, expected impact and rollback. Obtain explicit user direction for deployment, migrations, DNS, permissions, secrets and destructive actions. Do not create production resources merely to make a planning example concrete. Use least privilege, stage migrations and test row-level security with authorised/unauthorised roles. Never embed credentials in generated plans.

If the connector is absent, deliver an actionable plan or migration draft and clearly state that it has not been applied. Never fabricate tool calls or substitute a different account.
