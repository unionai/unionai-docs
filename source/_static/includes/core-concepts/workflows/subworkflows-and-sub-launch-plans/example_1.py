@union.workflow
def sub_wf(a: int, b: int) -> int:
    return t(a=a, b=b)

# Get the default launch plan of sub_wf, which we name sub_wf_lp
sub_wf_lp = LaunchPlan.get_or_create(sub_wf)

@union.workflow
def main_wf():
    # Invoke sub_wf directly.
    # An embedded subworkflow results.
    sub_wf(a=3, b=4)

    # Invoke sub_wf through its default launch plan, here called sub_wf_lp
    # An independent subworkflow results.
    sub_wf_lp(a=1, b=2)