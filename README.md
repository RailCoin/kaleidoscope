# kaleidoscope

multisig transaction management application

# WIP

does not work yet

# design decisions

this is a quick and dirty prototype. multiple simultaneous writers will lose
the earlier write because it's using s3 for persistence to avoid having to
run a real database.
