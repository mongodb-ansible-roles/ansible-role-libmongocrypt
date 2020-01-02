# frozen_string_literal: true

describe directory('/usr/include/mongocrypt') do
  it { should exist }
end

describe file('/usr/include/mongocrypt/mongocrypt-compat.h') do
  it { should exist }
end

describe file('/usr/include/mongocrypt/mongocrypt.h') do
  it { should exist }
end

describe file('/usr/include/mongocrypt/mongocrypt-export.h') do
  it { should exist }
end

describe file('/usr/lib/x86_64-linux-gnu/libmongocrypt.so') do
  it { should exist }
end
